<template>
  <!-- 人工智能AI助手 -->
  <div id="ai-global-toolbar">
    <!-- 弹出窗口 -->
    <div :class="isOpen ? 'ai-toolbar-wrap ai-toolbar-pen' : 'ai-toolbar-wrap'">
      <!--内层容器，包含弹出工具区域和工具按钮 定位是relative-->
      <div class="ai-toolbar-container">
        <div class="ai-toolbar-panel">
          <!-- 聊天窗口 -->
          <div class="ai-chat-container">
            <!-- 聊天标题 -->
            <div class="ai-title-panel">
              <div class="title">
                <h4>欢迎使用AI助手</h4>
                <span class="test">内测版</span>
              </div>
              <div>
                大语言模型来自：<a
                  href="https://www.deepseek.com/"
                  target="blank"
                  >DeepSeek-V3</a
                >
              </div>
            </div>
            <!-- 聊天内容框 -->
            <div class="ai-chat-content">
              <!-- 超出内容部分下拉框 -->
              <ChatDialogComponents :AI_OutList="ai_outputList" />
            </div>
          </div>
          <!-- 聊天输入 -->
          <div class="ai-chat-input-panel">
            <div class="ai-loading" v-if="ai_loading">AI思考中....请稍后</div>
            <div class="ai-input-commit">
              <el-input
                placeholder="请输入你的问题,并按Enter提问"
                v-model="user_input"
                @keyup.enter="NewStreamChat"
                clearable
              >
              </el-input>
              <div class="ai-button" title="发送提问" @click="NewStreamChat">
                <!-- 按钮图标 -->
                <svg
                  width="36"
                  height="36"
                  viewBox="0 0 36 36"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <rect
                    width="36"
                    height="36"
                    rx="18"
                    fill="#2454FF"
                    fill-opacity="0.06"
                  />
                  <path
                    d="M15.8602 20.4665L19.388 27.2923C19.6781 27.8536 20.5012 27.7871 20.6974 27.1866L25.8723 11.3524C26.0534 10.7983 25.5283 10.2733 24.9742 10.4544L9.14009 15.6292C8.53952 15.8255 8.47305 16.6486 9.03435 16.9387L15.8602 20.4665ZM15.8602 20.4665L18.5037 17.823"
                    stroke="#2454FF"
                    stroke-width="2.13626"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M19.2591 18.5782C19.6762 18.1611 19.6762 17.4848 19.2591 17.0677C18.842 16.6506 18.1657 16.6506 17.7485 17.0677L19.2591 18.5782ZM17.2477 14.1033L18.2629 13.7715L17.5993 11.7409L16.584 12.0727L17.2477 14.1033ZM15.3979 20.2275L15.8883 19.2786L15.3979 20.2275ZM9.03448 16.9387L9.5249 15.9898L9.03448 16.9387ZM15.8883 19.2786L9.5249 15.9898L8.54406 17.8875L14.9075 21.1764L15.8883 19.2786ZM16.9837 20.8537L19.2591 18.5782L17.7485 17.0677L15.4731 19.3431L16.9837 20.8537ZM9.47203 16.6445L12.5514 15.6381L11.8878 13.6075L8.80841 14.6139L9.47203 16.6445ZM12.5514 15.6381L17.2477 14.1033L16.584 12.0727L11.8878 13.6075L12.5514 15.6381ZM14.9075 21.1764C15.596 21.5322 16.4356 21.4017 16.9837 20.8537L15.4731 19.3431C15.5827 19.2335 15.7506 19.2074 15.8883 19.2786L14.9075 21.1764ZM9.5249 15.9898C9.80555 16.1348 9.77232 16.5463 9.47203 16.6445L8.80841 14.6139C7.30697 15.1046 7.14082 17.1623 8.54406 17.8875L9.5249 15.9898Z"
                    fill="#24EFFE"
                  />
                  <path
                    d="M19.2589 18.5783C19.676 18.1611 19.676 17.4848 19.2589 17.0677C18.8417 16.6506 18.1654 16.6506 17.7483 17.0677L19.2589 18.5783ZM12.5512 15.6381L13.5665 15.3063L12.9028 13.2757L11.8875 13.6075L12.5512 15.6381ZM15.3977 20.2275L14.9073 21.1764L15.3977 20.2275ZM15.8881 19.2786L9.52467 15.9898L8.54384 17.8876L14.9073 21.1764L15.8881 19.2786ZM16.9834 20.8537L19.2589 18.5783L17.7483 17.0677L15.4729 19.3431L16.9834 20.8537ZM9.47181 16.6445L12.5512 15.6381L11.8875 13.6075L8.80818 14.6139L9.47181 16.6445ZM14.9073 21.1764C15.5958 21.5322 16.4354 21.4017 16.9834 20.8537L15.4729 19.3431C15.5825 19.2335 15.7504 19.2074 15.8881 19.2786L14.9073 21.1764ZM9.52467 15.9898C9.80532 16.1348 9.77209 16.5464 9.47181 16.6445L8.80818 14.6139C7.30675 15.1046 7.1406 17.1623 8.54384 17.8876L9.52467 15.9898Z"
                    fill="#00BCFF"
                  />
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M19.6605 17.4694C19.8558 17.6647 19.8558 17.9813 19.6605 18.1766L16.9834 20.8537C16.4353 21.4017 15.5957 21.5322 14.9072 21.1764L10.2522 18.7706L11.233 16.8728L15.6568 19.1591L18.15 16.666C18.3452 16.4707 18.6618 16.4707 18.8571 16.666L19.6605 17.4694Z"
                    fill="#2454FF"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
        <div class="ai-toolbar-buttons">
          <div class="ai-tbar-list">
            <div class="ai-tbar-item" @click="openAIWindows">
              <i class="tbar_icon">Ai</i>
              <em class="tab-text">AI助手</em>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, nextTick } from "vue";
import ChatDialogComponents from "@/components/ChatDialogComponents.vue";

const isOpen = ref(false);
const user_input = ref("");
const ai_output = ref("");
const ai_outputList = ref([]);
const ai_loading = ref(false);
const init_message = ref([]);

const openAIWindows = () => {
  isOpen.value = !isOpen.value;
};

const scrollToBottom = () => {
  nextTick(() => {
    var container = document.querySelector(".ai-chat-content");
    container.scrollTop = container.scrollHeight;
  });
};

const replaceMathSymbols = (inputStr) => {
  let replacedStr;
  replacedStr = inputStr
    .replace(/\\\[(\s*)/g, "$$")
    .replace(/(\s*)\\\]/g, "$$");
  replacedStr = replacedStr
    .replace(/\\\((\s*)/g, "$")
    .replace(/(\s*)\\\)/g, "$");
  return replacedStr;
};

const NewStreamChat = async () => {
  if (ai_loading.value) {
    return;
  }
  ai_loading.value = true;

  try {
    const prompt = user_input.value;
    user_input.value = "";
    ai_outputList.value.push({ role: "user", content: prompt });
    scrollToBottom();
    init_message.value.push({ role: "user", content: prompt });

    const response = await fetch("http://localhost:8000/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Authorization: "Bearer " + "key",
      },
      body: JSON.stringify({
        messages: init_message.value,
        // model: "deepseek-chat",
        max_tokens: 2048,
        temperature: 0.1,
        stream: true,
      }),
    });

    if (!response.body) {
      throw new Error("服务器未返回流数据");
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let buffer = "";

    ai_outputList.value.push({ role: "assistant", content: "" });

    while (true) {
      const { done, value } = await reader.read();
      if (done) {
        break;
      }
      const chunk = decoder.decode(value, { stream: true });
      console.log("流数据：", chunk);

      buffer += chunk;

      const lines = buffer.split("\n");
      buffer = lines.pop();
      for (const line of lines) {
        if (line.startsWith("data: ")) {
          const jsonStr = line.slice(6).trim();
          if (jsonStr !== "[DONE]") {
            try {
              const jsonData = JSON.parse(jsonStr);
              const content = jsonData?.choices[0]?.delta?.content || "";
              if (content) {
                ai_output.value += content;
                ai_outputList.value[ai_outputList.value.length - 1].content +=
                  content;
                ai_outputList.value[ai_outputList.value.length - 1].content =
                  replaceMathSymbols(
                    ai_outputList.value[ai_outputList.value.length - 1].content
                  );
                
                scrollToBottom();
              }
            } catch (error) {
              console.error("解析 JSON 数据失败:", error, line);
            }
          } else {
            init_message.value.push({
              role: "assistant",
              content: ai_output.value,
            });
            scrollToBottom();
          }
        }
      }
    }
    ai_outputList.value[ai_outputList.value.length - 1].content =
      replaceMathSymbols(
        ai_outputList.value[ai_outputList.value.length - 1].content
      );
    ai_loading.value = false;
  } catch (error) {
    console.error("流数据请求失败:", error);
  } finally {
    console.log(ai_outputList.value);
    ai_loading.value = false;
  }
};
</script>

<style scoped>
#ai-global-toolbar {
  display: block;
}
.ai-toolbar-wrap {
  position: fixed;
  height: 100%;
  top: 0;
  right: -600px;
  z-index: 2999;
  transition: right 0.5s;
}

.ai-toolbar-pen {
  right: 0px;
}

.ai-toolbar-container {
  position: relative;
  width: 600px;
  height: 100%;
}

.ai-toolbar-panel {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 600px;
  height: 100%;
  background-color: #fcfbfb;
  border-left: solid 4px rgb(74, 175, 241);
  z-index: 99;
}

.ai-toolbar-buttons {
  position: absolute;
  top: 0;
  left: 1px;
  height: 100%;
}

.ai-tbar-list {
  position: absolute;
  top: 50%;
  right: 0;
  margin-top: -61px;
  width: 35px;
}

.ai-tbar-item {
  position: relative;
  width: 35px;
  height: 35px;
  margin-bottom: 1px;
  cursor: pointer;
  text-align: center;
  line-height: 35px;
  border-radius: 3px 0 0 3px;
}

.ai-tbar-item .tbar_icon {
  position: relative;
  z-index: 5;
  width: 34px;
  height: 35px;
  display: block;
  margin-left: 1px;
  background-color: rgb(140, 143, 145);
  border: solid 1px rgba(255, 255, 255, 1);
  border-radius: 5px 0 0 5px;
  color: #ffffff;
  font-size: 20px;
}

.ai-tbar-item .tbar_icon:hover {
  background-color: rgb(74, 175, 241);
  border-left: solid 1px rgba(255, 255, 255, 0);
  border-radius: 0;
}

.tab-text {
  width: 62px;
  height: 35px;
  line-height: 35px;
  color: #fff;
  text-align: center;
  font-family: 微软雅黑;
  position: absolute;
  left: 35px;
  font-size: 12px;
  font-style: normal;
  z-index: 4;
  top: 0;
  background-color: rgb(74, 175, 241);
  border: solid 1px #ffffff;
  border-radius: 5px 0 0 5px;
  border-radius: 3px 0 0 3px;
  transition: left 0.3s;
}

.ai-tbar-item .tbar_icon:hover + .tab-text {
  left: -60px;
}

/* AI区域内容样式 */
/* 标题部分 */
.ai-title-panel {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 30px;
}

.ai-title-panel > div {
  display: flex;
  justify-content: center;
}

.title {
  margin-top: 30px;
}
.title h4 {
  font-weight: 700;
}

.title .test {
  border: 1px solid rgb(3, 150, 248);
  color: rgb(3, 150, 248);
  border-radius: 3px;
  padding: 0 3px;
  height: 18px;
  line-height: 18px;
  margin-left: 5px;
}

/* 内容部分 */
.ai-chat-content {
  position: relative;
  padding: 10px 10px;
  background: #ffffff;
  height: calc(100vh - 115px - 150px);
  overflow-y: auto;
  font-size: 16px;
  color: #000;
}

.chat-dialog {
  padding: 0 10px;
}

/* 动态html样式不生效 */
:deep(.question) {
  font-weight: 700;
  margin-top: 10px;
}
/* 聊天输入 */

.ai-chat-input-panel {
  display: flex;
  flex-direction: column;
  margin-bottom: 70px;
  padding: 10px;
}

.ai-loading {
  font-size: 15px;
  line-height: 16px;
  margin: 10px 0;
}

.ai-input-commit {
  display: flex;
  width: 100%;
}

.ai-button {
  margin-left: 5px;
  cursor: pointer;
}
.ai-button svg {
  width: 40px;
  height: 40px;
}

a {
  text-decoration: none;
}

a:hover {
  color: #f15323;
}

/* 自定义滚动条的整体样式 */
::-webkit-scrollbar {
  width: 12px;
}

/* 自定义滚动轨迹的样式 */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* 自定义滚动滑块的样式 */
::-webkit-scrollbar-thumb {
  background-color: rgb(99, 188, 247);
  border-radius: 6px;
  border: 3px solid transparent;
  background-clip: content-box;
}

/* 当鼠标悬停在滚动滑块上时的样式 */
::-webkit-scrollbar-thumb:hover {
  background-color: rgb(45, 165, 246);
}
</style>