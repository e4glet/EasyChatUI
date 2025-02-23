<template>
  <div class="home">
    <el-input
      v-model="user_input"
      :autosize="{ minRows: 2, maxRows: 4 }"
      type="textarea"
      placeholder="请输入内容"
    />
    <el-button type="primary" @click="handlerClick">测试</el-button>
    <div v-if="loading">加载中...</div>
    <div v-else>
      <p>{{ response }}</p>
    </div>
    <ChatAIComponentsVue/>
  </div>
</template>

<script setup>
import ChatAIComponentsVue from '@/components/ChatAIComponents.vue';
import { ref } from "vue";
import { nextTick } from "vue";

const response = ref(""); // 实时响应内容
const loading = ref(false); // 加载状态
const user_input = ref(""); // 用户输入
const init_message = ref([]); // 对话历史

const handlerClick = async () => {
  loading.value = true;
  response.value = "";
  const prompt = user_input.value;
  user_input.value = "";
  
  // ✅ 使用新数组触发响应式更新
  init_message.value = [
    ...init_message.value,
    { role: "user", content: prompt }
  ];

  try {
    const res = await fetch("http://localhost:8000/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        messages: init_message.value, // ✅ 发送完整历史
        max_tokens: 512,
        temperature: 0.7,
        stream: true,
      }),
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    loading.value = false; 

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) {
        console.log("[流式数据] 完成");
        break;
      }

      buffer += decoder.decode(value, { stream: true });
      const chunks = buffer.split(/data: /); // ✅ 更稳定的分割逻辑
      // const chunks = buffer.split("\n")
      buffer = chunks.pop() || "";

      for (const chunk of chunks) {
        const line = chunk.trim();
        if (!line) continue;

        console.log("流式数据：\n", line);

        if (line === "[DONE]") {
          console.log("[流式数据] 接收完成");
          // ✅ 使用新数组更新历史
          init_message.value = [
            ...init_message.value,
            { role: "assistant", content: response.value }
          ];
          loading.value = false;
          await nextTick(); // 确保UI更新
          return;
        }

        try {
          const jsonData = JSON.parse(line);
          const content = jsonData.choices[0]?.delta?.content || "";
          response.value += content;
          await nextTick(); // 确保UI更新          
        } catch (e) {
          console.error("[Stream Parse Error]", e, "Data:", line);
        }
      }
    }
  } catch (error) {
    console.error("[Request Failed]", error);
  } finally {
    loading.value = false;    
  }
};
</script>


