# server/src/model_manager.py
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    StoppingCriteria,
    StoppingCriteriaList,
    TextStreamer
)
from typing import Optional, List, Dict
from loguru import logger
from pathlib import Path

# 停止条件：根据 tokens 停止
class StopOnTokens(StoppingCriteria):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer  # 初始化 tokenizer

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [self.tokenizer.eos_token_id]  # 使用 eos_token_id 作为停止条件
        return input_ids[0][-1] in stop_ids

# transformers模型管理器
import threading
class ModelManager:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.loaded_model_name = None
        self.stop_flag = False # 停止标志，控制模型停止输出
        self.stop_event = threading.Event()  # 新增线程事件
        self.is_gguf = False  # 新增模型类型标识

    # 加载模型
    def load_model(self, model_path: Path):
        """加载模型和tokenizer"""
        try:
            if model_path.suffix == '.gguf':
                self.is_gguf = True
                if not hasattr(self, 'gguf_manager'):
                    self.gguf_manager = GGUFModelManager()
                self.gguf_manager.load_model(model_path)
            else:
                self.is_gguf = False
                # 先使用 Path 对象获取模型名称
                self.loaded_model_name = model_path.stem  # ✅ 此处直接使用 Path 对象

                # 再转换为字符串供 Hugging Face 使用
                model_path_str = str(model_path)
                
                logger.info(f"Loading model from {model_path_str}...")
                
                self.tokenizer = AutoTokenizer.from_pretrained(
                    model_path_str,
                    trust_remote_code=True
                )
                
                self.model = AutoModelForCausalLM.from_pretrained(
                    model_path_str,
                    device_map="auto",
                    torch_dtype=torch.float16,
                    # load_in_4bit=True,
                    trust_remote_code=True
                )
                
                logger.success(f"Model {self.loaded_model_name} loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    # 生成文本
    def generate(
        self,
        prompt: str,
        max_length: int = 2048,  # 减少最大生成长度
        temperature: float = 0.7,  # 保持适中随机性
        top_p: float = 0.9,  # 控制多样性
        repetition_penalty: float = 1.2  # 添加重复惩罚
    ) -> str:
        if self.is_gguf:
            # 将prompt转换为消息格式
            messages = [{"role": "user", "content": prompt}]
            return self.gguf_manager.generate_gguf(messages, **kwargs)
        else:
            """生成文本"""
            if not self.model or not self.tokenizer:
                raise ValueError("Model not loaded")
            
            # 编码输入并生成 attention_mask
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,  # 启用填充
                truncation=True  # 启用截断
            ).to(self.model.device)
            
            # 显式设置 attention_mask
            attention_mask = inputs["attention_mask"]

            try:
                # 初始化停止条件
                stop_criteria = StopOnTokens(self.tokenizer)
                
                outputs = self.model.generate(
                    inputs.input_ids,
                    attention_mask=attention_mask,  # 添加 attention_mask
                    max_length=max_length,
                    temperature=temperature,
                    top_p=top_p,
                    repetition_penalty=repetition_penalty,  # 添加重复惩罚
                    do_sample=True,
                    stopping_criteria=StoppingCriteriaList([stop_criteria]),  # 使用停止条件
                    pad_token_id=self.tokenizer.eos_token_id
                )
                
                # 解码输出
                response = self.tokenizer.decode(
                    outputs[0],
                    skip_special_tokens=True
                )
                print(response)
                
                logger.info(f"Input: {prompt}")
                logger.info(f"Output: {response}")
                return response
            
            except Exception as e:
                logger.error(f"Generation failed: {str(e)}")
                raise ValueError("Failed to generate text")
    
    # 流式生成文本
    def generate_stream(
        self,
        messages: List[Dict],  # 实际接收的是 ChatMessage 对象列表
        max_length: int = 2048,
        temperature: float = 0.7,
        top_p: float = 0.9,
        repetition_penalty: float = 1.2
    ):
        if self.is_gguf:
            return self.gguf_manager.generate_gguf_stream(messages, **kwargs)
        else:
            """流式生成文本（最终修正版）"""
            # 构造符合模型格式的 prompt  
            # 1. 构造 prompt
            full_prompt = ""
            for msg in messages:  # ✅ 遍历全部消息
                if msg.role == "system":
                    full_prompt += f"system: {msg.content}\n"
                elif msg.role == "user":
                    full_prompt += f"user: {msg.content}\n"
                elif msg.role == "assistant":
                    full_prompt += f"assistant: {msg.content}\n"
            full_prompt += "assistant: <think>"  # 添加当前回复的开头

            # 2. 编码输入
            inputs = self.tokenizer(
                full_prompt,
                return_tensors="pt",
                padding=True,
                truncation=True
            ).to(self.model.device)
            
            # 3. 使用 TextIteratorStreamer
            from transformers import TextIteratorStreamer
            streamer = TextIteratorStreamer(
                self.tokenizer,
                skip_prompt=True,
                skip_special_tokens=True
            )

            # 4. 在独立线程中生成
            import threading
            generation_kwargs = {
                **inputs,  # 直接传入 input_ids 和 attention_mask
                "max_new_tokens": max_length,  # ✅ 关键修正：使用 max_new_tokens 而非 max_length
                "temperature": temperature,
                "top_p": top_p,
                "repetition_penalty": repetition_penalty,
                "do_sample": True,
                "stopping_criteria": StoppingCriteriaList([StopOnTokens(self.tokenizer)]),
                "pad_token_id": self.tokenizer.eos_token_id,
                "streamer": streamer
            }

            try:
                self.reset_stop_flag()  # 新增：每次生成前重置标志
                
                thread = threading.Thread(target=self.model.generate, kwargs=generation_kwargs)
                thread.start()

                # 修改后的生成循环
                for token in streamer:
                    if self.stop_flag or self.stop_event.is_set():
                        logger.info("Generation stopped by user")
                        break
                    yield token
            
            finally:
                self.reset_stop_flag()  # 确保异常时也能重置

    # 停止生成
    def stop_generation(self):
        """停止生成（线程安全版）"""
        self.stop_flag = True
        self.stop_event.set()
        logger.info("Generation stop requested")
        return True
    
    def reset_stop_flag(self):
        """重置停止标志（在每次生成开始时调用）"""
        self.stop_flag = False
        self.stop_event.clear()
    

# GGUF模型管理模块
from llama_cpp import Llama

class GGUFModelManager:
    def __init__(self):
        self.llm = None
        self.loaded_model_name = None
        
    def load_model(self, model_path: Path):
        try:
            self.loaded_model_name = model_path.stem
            logger.info(f"Loading GGUF model from {model_path}...")
            
            self.llm = Llama(
                model_path=str(model_path),
                n_ctx=2048,
                n_threads=4,
                n_gpu_layers=50 if torch.cuda.is_available() else 0,
                verbose=False
            )
            logger.success(f"GGUF Model {self.loaded_model_name} loaded")
            
        except Exception as e:
            logger.error(f"GGUF load failed: {str(e)}")
            raise

    def generate_gguf(self, messages, max_length=512, **kwargs):
        full_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages]) + "\nassistant:"
        
        output = self.llm.create_chat_completion(
            messages=messages,
            max_tokens=max_length,
            stream=False,
            temperature=kwargs.get('temperature', 0.7),
            top_p=kwargs.get('top_p', 0.9),
            repeat_penalty=kwargs.get('repetition_penalty', 1.2)
        )
        return output['choices'][0]['message']['content']

    def generate_gguf_stream(self, messages, max_length=512, **kwargs):
        full_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages]) + "\nassistant:"
        print("gguf流式输出")
        
        stream = self.llm.create_chat_completion(
            messages=messages,
            max_tokens=max_length,
            stream=True,
            temperature=kwargs.get('temperature', 0.7),
            top_p=kwargs.get('top_p', 0.9),
            repeat_penalty=kwargs.get('repetition_penalty', 1.2)
        )
        for chunk in stream:
            if 'content' in chunk['choices'][0]['delta']:
                yield chunk['choices'][0]['delta']['content']

# 单例实例
model_manager = ModelManager()