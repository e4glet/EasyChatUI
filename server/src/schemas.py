# server/src/schemas.py
from pydantic import BaseModel
from typing import Optional, List, Dict

# 消息模型
class ChatMessage(BaseModel):
    role: str  # "user" 或 "assistant"
    content: str

# 请求模型
class ChatRequest(BaseModel):
    messages: List[ChatMessage]  # 消息列表
    max_tokens: Optional[int] = 2048  # 最大生成长度
    temperature: Optional[float] = 0.1  # 随机性
    top_p: Optional[float] = 0.1  # 多样性
    repetition_penalty: Optional[float] = 1.2  # 重复惩罚
    stream: Optional[bool] = False  # 是否启用流式输出
    use_search: Optional[bool] = False  # 总开关
    search_provider: Optional[str] = "bing"  # 指定搜索引擎

# 停止请求模型
class StopRequest(BaseModel):
    confirm: bool = True