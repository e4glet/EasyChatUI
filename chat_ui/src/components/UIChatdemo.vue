<template>
  <div class="app-container">
    <BarComponents />
    <div class="chat-container">
      <!-- 标题和Logo -->
      <div class="header">
        <el-icon class="logo" :size="60">
          <svg
            viewBox="0 0 30 30"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
          >
            <path
              id="path"
              d="M27.501 8.46875C27.249 8.3457 27.1406 8.58008 26.9932 8.69922C26.9434 8.73828 26.9004 8.78906 26.8584 8.83398C26.4902 9.22852 26.0605 9.48633 25.5 9.45508C24.6787 9.41016 23.9785 9.66797 23.3594 10.2969C23.2275 9.52148 22.79 9.05859 22.125 8.76172C21.7764 8.60742 21.4238 8.45312 21.1807 8.11719C21.0098 7.87891 20.9639 7.61328 20.8779 7.35156C20.8242 7.19336 20.7695 7.03125 20.5879 7.00391C20.3906 6.97266 20.3135 7.13867 20.2363 7.27734C19.9258 7.84375 19.8066 8.46875 19.8174 9.10156C19.8447 10.5234 20.4453 11.6562 21.6367 12.4629C21.7725 12.5547 21.8076 12.6484 21.7646 12.7832C21.6836 13.0605 21.5869 13.3301 21.501 13.6074C21.4473 13.7852 21.3662 13.8242 21.1768 13.7461C20.5225 13.4727 19.957 13.0684 19.458 12.5781C18.6104 11.7578 17.8438 10.8516 16.8877 10.1426C16.6631 9.97656 16.4395 9.82227 16.207 9.67578C15.2314 8.72656 16.335 7.94727 16.5898 7.85547C16.8574 7.75977 16.6826 7.42773 15.8193 7.43164C14.957 7.43555 14.167 7.72461 13.1611 8.10938C13.0137 8.16797 12.8594 8.21094 12.7002 8.24414C11.7871 8.07227 10.8389 8.0332 9.84766 8.14453C7.98242 8.35352 6.49219 9.23633 5.39648 10.7441C4.08105 12.5547 3.77148 14.6133 4.15039 16.7617C4.54883 19.0234 5.70215 20.8984 7.47559 22.3633C9.31348 23.8809 11.4307 24.625 13.8457 24.4824C15.3125 24.3984 16.9463 24.2012 18.7881 22.6406C19.2529 22.8711 19.7402 22.9629 20.5498 23.0332C21.1729 23.0918 21.7725 23.002 22.2373 22.9062C22.9648 22.752 22.9141 22.0781 22.6514 21.9531C20.5186 20.959 20.9863 21.3633 20.5605 21.0371C21.6445 19.752 23.2783 18.418 23.917 14.0977C23.9668 13.7539 23.9238 13.5391 23.917 13.2598C23.9131 13.0918 23.9512 13.0254 24.1445 13.0059C24.6787 12.9453 25.1973 12.7988 25.6738 12.5352C27.0557 11.7793 27.6123 10.5391 27.7441 9.05078C27.7637 8.82422 27.7402 8.58789 27.501 8.46875ZM15.46 21.8613C13.3926 20.2344 12.3906 19.6992 11.9766 19.7227C11.5898 19.7441 11.6592 20.1875 11.7441 20.4766C11.833 20.7617 11.9492 20.959 12.1123 21.209C12.2246 21.375 12.3018 21.623 12 21.8066C11.334 22.2207 10.1768 21.668 10.1221 21.6406C8.77539 20.8477 7.64941 19.7988 6.85547 18.3652C6.08984 16.9844 5.64453 15.5039 5.57129 13.9238C5.55176 13.541 5.66406 13.4062 6.04297 13.3379C6.54199 13.2461 7.05762 13.2266 7.55664 13.2988C9.66602 13.6074 11.4619 14.5527 12.9668 16.0469C13.8262 16.9004 14.4766 17.918 15.1465 18.9121C15.8584 19.9688 16.625 20.9746 17.6006 21.7988C17.9443 22.0879 18.2197 22.3086 18.4824 22.4707C17.6895 22.5586 16.3652 22.5781 15.46 21.8613ZM16.4502 15.4805C16.4502 15.3105 16.5859 15.1758 16.7568 15.1758C16.7949 15.1758 16.8301 15.1836 16.8613 15.1953C16.9033 15.2109 16.9424 15.2344 16.9727 15.2695C17.0273 15.3223 17.0586 15.4004 17.0586 15.4805C17.0586 15.6504 16.9229 15.7852 16.7529 15.7852C16.582 15.7852 16.4502 15.6504 16.4502 15.4805ZM19.5273 17.0625C19.3301 17.1426 19.1328 17.2129 18.9434 17.2207C18.6494 17.2344 18.3281 17.1152 18.1533 16.9688C17.8828 16.7422 17.6895 16.6152 17.6074 16.2168C17.5732 16.0469 17.5928 15.7852 17.623 15.6348C17.6934 15.3105 17.6152 15.1035 17.3877 14.9141C17.2012 14.7598 16.9658 14.7188 16.7061 14.7188C16.6094 14.7188 16.5205 14.6758 16.4541 14.6406C16.3457 14.5859 16.2568 14.4512 16.3418 14.2852C16.3691 14.2324 16.501 14.1016 16.5322 14.0781C16.8838 13.877 17.29 13.9434 17.666 14.0938C18.0146 14.2363 18.2773 14.498 18.6562 14.8672C19.0439 15.3145 19.1133 15.4395 19.334 15.7734C19.5078 16.0371 19.667 16.3066 19.7754 16.6152C19.8408 16.8066 19.7559 16.9648 19.5273 17.0625Z"
              fill-rule="nonzero"
              fill="#4D6BFE"
            ></path>
          </svg>
        </el-icon>
        <h1 class="title">欢迎使用deepseek R1</h1>
      </div>

      <!-- 聊天内容区域 -->
      <div class="chat-content">
        <!-- 超出内容部分下拉框 -->
        <ChatDialogComponents
          :AI_OutList="ai_outputList"
          :AI_StopByUser="isStoppedByUser"
        />
        <!-- 添加新对话按钮 -->
        <div
          v-if="ai_outputList.length > 0"
          class="new-chat-button"
          @click="startNewChat"
        >
          <div class="new-chat-content">
            <svg
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M5.856 17.121a.979.979 0 0 1-.327-.06.839.839 0 0 1-.283-.177.739.739 0 0 1-.187-.255.724.724 0 0 1-.07-.303l-.02-1.609a4.663 4.663 0 0 1-1.446-.455 4.252 4.252 0 0 1-.637-.401c-.199-.146-.385-.31-.553-.492a4.442 4.442 0 0 1-.45-.577 4.303 4.303 0 0 1-.327-.637 3.823 3.823 0 0 1-.206-.686 3.729 3.729 0 0 1-.064-.704V6.478c0-.261.025-.516.077-.771a4.43 4.43 0 0 1 .244-.747 4.062 4.062 0 0 1 .932-1.28c.2-.183.418-.347.65-.493.23-.145.482-.267.739-.364a4.21 4.21 0 0 1 .81-.225c.27-.054.553-.078.835-.078H8.55c.103 0 .2.018.29.054a.7.7 0 0 1 .411.376.667.667 0 0 1-.161.766.736.736 0 0 1-.25.151.764.764 0 0 1-.29.055H5.573c-.186 0-.366.012-.54.049-.18.03-.353.079-.52.145-.167.061-.328.14-.482.237-.148.091-.29.2-.418.316a2.897 2.897 0 0 0-.347.388c-.097.14-.187.286-.257.444a2.473 2.473 0 0 0-.206.977v4.287c0 .17.013.333.051.503a2.549 2.549 0 0 0 .772 1.33 2.721 2.721 0 0 0 .913.559c.167.066.347.115.527.152.18.03.36.048.546.048a.904.904 0 0 1 .61.23.848.848 0 0 1 .194.262.84.84 0 0 1 .07.303l.007.99 1.915-1.293a2.877 2.877 0 0 1 1.64-.492h2.372c.186 0 .366-.018.54-.048.18-.03.353-.08.52-.146.168-.067.329-.146.483-.237.148-.091.29-.2.418-.316.128-.121.244-.249.347-.388a2.8 2.8 0 0 0 .257-.444 2.47 2.47 0 0 0 .206-.977V8.585a.646.646 0 0 1 .225-.492.679.679 0 0 1 .244-.152.814.814 0 0 1 .585 0c.09.03.174.085.244.152a.657.657 0 0 1 .225.492V10.8c0 .261-.032.516-.083.771a4.192 4.192 0 0 1-.245.74c-.109.244-.244.468-.398.687a3.735 3.735 0 0 1-.534.6c-.2.183-.418.347-.65.493a4.134 4.134 0 0 1-.738.364 4.7 4.7 0 0 1-.81.225c-.27.054-.553.079-.836.079h-1.877c-.604 0-1.144.164-1.633.491l-2.54 1.713a.913.913 0 0 1-.514.157z"
                fill="currentColor"
              ></path>
              <path
                d="M15.866 4.125h-4.174c-.41 0-.741.313-.741.7 0 .387.332.7.741.7h4.174c.41 0 .742-.313.742-.7 0-.387-.332-.7-.742-.7z"
                fill="currentColor"
              ></path>
              <path
                d="M14.537 2.932c0-.396-.34-.717-.759-.717s-.758.32-.758.717v3.786c0 .396.34.717.758.717.42 0 .76-.321.76-.717V2.932z"
                fill="currentColor"
              ></path>
            </svg>
            <span>开启新对话</span>
          </div>
        </div>
      </div>

      <!-- 输入区域 -->
      <div class="input-area">
        <div class="input-container">
          <el-input
            class="chat-input"
            v-model="user_input"
            type="textarea"
            :rows="2"
            placeholder="输入你的问题..."
            @keydown.enter.exact.prevent="sendMessage"
          />
        </div>
        <div class="btn-area">
          <!-- 启用深度思考 -->
          <div
            class="ds-button mgr-10"
            :class="{ 'ds-button__enable': isActiveDeepThink }"
            @click="toggleDeepThink"
          >
            <div class="ds-button__icon">
              <svg
                width="20"
                height="20"
                viewBox="0 0 20 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M2.656 17.344c-1.016-1.015-1.15-2.75-.313-4.925.325-.825.73-1.617 1.205-2.365L3.582 10l-.033-.054c-.5-.799-.91-1.596-1.206-2.365-.836-2.175-.703-3.91.313-4.926.56-.56 1.364-.86 2.335-.86 1.425 0 3.168.636 4.957 1.756l.053.034.053-.034c1.79-1.12 3.532-1.757 4.957-1.757.972 0 1.776.3 2.335.86 1.014 1.015 1.148 2.752.312 4.926a13.892 13.892 0 0 1-1.206 2.365l-.034.054.034.053c.5.8.91 1.596 1.205 2.365.837 2.175.704 3.911-.311 4.926-.56.56-1.364.861-2.335.861-1.425 0-3.168-.637-4.957-1.757L10 16.415l-.053.033c-1.79 1.12-3.532 1.757-4.957 1.757-.972 0-1.776-.3-2.335-.86zm13.631-4.399c-.187-.488-.429-.988-.71-1.492l-.075-.132-.092.12a22.075 22.075 0 0 1-3.968 3.968l-.12.093.132.074c1.308.734 2.559 1.162 3.556 1.162.563 0 1.006-.138 1.298-.43.3-.3.436-.774.428-1.346-.008-.575-.159-1.264-.449-2.017zm-6.345 1.65l.058.042.058-.042a19.881 19.881 0 0 0 4.551-4.537l.043-.058-.043-.058a20.123 20.123 0 0 0-2.093-2.458 19.732 19.732 0 0 0-2.458-2.08L10 5.364l-.058.042A19.883 19.883 0 0 0 5.39 9.942L5.348 10l.042.059c.631.874 1.332 1.695 2.094 2.457a19.74 19.74 0 0 0 2.458 2.08zm6.366-10.902c-.293-.293-.736-.431-1.298-.431-.998 0-2.248.429-3.556 1.163l-.132.074.12.092a21.938 21.938 0 0 1 3.968 3.968l.092.12.074-.132c.282-.504.524-1.004.711-1.492.29-.753.442-1.442.45-2.017.007-.572-.129-1.045-.429-1.345zM3.712 7.055c.202.514.44 1.013.712 1.493l.074.13.092-.119a21.94 21.94 0 0 1 3.968-3.968l.12-.092-.132-.074C7.238 3.69 5.987 3.262 4.99 3.262c-.563 0-1.006.138-1.298.43-.3.301-.436.774-.428 1.346.007.575.159 1.264.448 2.017zm0 5.89c-.29.753-.44 1.442-.448 2.017-.008.572.127 1.045.428 1.345.293.293.736.431 1.298.431.997 0 2.247-.428 3.556-1.162l.131-.074-.12-.093a21.94 21.94 0 0 1-3.967-3.968l-.093-.12-.074.132a11.712 11.712 0 0 0-.71 1.492z"
                  fill="currentColor"
                  stroke="currentColor"
                  stroke-width=".1"
                ></path>
                <path
                  d="M10.706 11.704A1.843 1.843 0 0 1 8.155 10a1.845 1.845 0 1 1 2.551 1.704z"
                  fill="currentColor"
                  stroke="currentColor"
                  stroke-width=".2"
                ></path>
              </svg>
            </div>
            <span class="ds-button__text">深度思考 (R1)</span>
          </div>
          <!-- 启用联网搜索 -->
          <div
            class="ds-button mgr-10"
            :class="{ 'ds-button__enable': isActiveSearch }"
            @click="toggleSearch"
          >
            <div class="ds-button__icon">
              <svg
                width="20"
                height="20"
                viewBox="0 0 20 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle
                  cx="10"
                  cy="10"
                  r="9"
                  stroke="currentColor"
                  stroke-width="1.8"
                ></circle>
                <path
                  d="M10 1c1.657 0 3 4.03 3 9s-1.343 9-3 9M10 19c-1.657 0-3-4.03-3-9s1.343-9 3-9M1 10h18"
                  stroke="currentColor"
                  stroke-width="1.8"
                ></path>
              </svg>
            </div>
            <span class="ds-button__text">联网搜索</span>
          </div>
          <div class="ds-button-area">
            <div v-if="!ai_loading" class="send-area" @click="sendMessage">
              <div
                class="ds-icon"
                style="font-size: 16px; width: 16px; height: 16px"
              >
                <svg
                  data-v-65317e7f=""
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 1024 1024"
                >
                  <path
                    fill="currentColor"
                    d="m64 448 832-320-128 704-446.08-243.328L832 192 242.816 545.472zm256 512V657.024L512 768z"
                  ></path>
                </svg>
              </div>
            </div>
            <div class="send-area" v-else @click="stopOutput">
              <div class="ds-icon-stop">
                <!-- 停止输出按钮 -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="tip_msg">内容由 AI 生成，请仔细甄别</div>
    </div>
  </div>
</template>

<script setup>
import BarComponents from "./BarComponents.vue";
import { ref, reactive, computed, onMounted, nextTick } from "vue";
import ChatDialogComponents from "@/components/ChatDialogComponents.vue";
import SystemStatus from "@/components/SystemStatus.vue";

// 系统提示词
const SYSTEM_PROMPT = {
  role: "system",
  content:
    "你是一个AI助手,名为deepseek R1。你非常专业、友好且富有同理心。你会以简洁清晰的方式回答问题,并始终保持谦逊和真诚。当你不确定某件事时,你会坦诚地承认。你会避免任何有害或不当的内容。",
};
const user_input = ref("");
const ai_output = ref("");
const ai_outputList = ref([]); // 修改这里：使用 const 并确保是 ref
const ai_loading = ref(false);
const init_message = ref([]);
const isActiveDeepThink = ref(true);
const isActiveSearch = ref(false);
const chatContent = ref(null); // 聊天内容区域自动滚动
// 新增状态变量
const isStoppedByUser = ref(false);

// 添加开始时间和token计数的变量
const startTime = ref(0);
const totalTokens = ref(0);

// 是否启用深度思考
const toggleDeepThink = () => {
  isActiveDeepThink.value = !isActiveDeepThink.value;
};

// 是否启用联网搜索
const toggleSearch = () => {
  isActiveSearch.value = !isActiveSearch.value;
};

const scrollToBottom = () => {
  nextTick(() => {
    var container = document.querySelector(".chat-content");
    container.scrollTop = container.scrollHeight;
  });
};
//优化
// const scrollToBottom = async () => {
//   await nextTick()
//   chatContent.value.scrollTop = chatContent.value.scrollHeight
// }

// 修改processAIResponse函数
const processAIResponse = (content, isCompleting = false) => {
  const thinkEndIndex = content.indexOf("</think>");
  let thinking = content;
  let answer = "";
  let isThinkedAnswer = false;

  if (thinkEndIndex > -1) {
    // 包含</think>标签时进行分割
    thinking = content.slice(0, thinkEndIndex).trim();
    answer = content.slice(thinkEndIndex + 8).trim(); // +8 跳过</think>标签及可能的空格
    isThinkedAnswer = true;
  } else if (isCompleting) {
    // 如果是最后处理且没有</think>标签,将所有内容移到answer
    thinking = "";
    answer = content;
    isThinkedAnswer = false;
  }

  return {
    thinking,
    answer,
    isThinkedAnswer,
    isStopped: isStoppedByUser.value,
  };
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

const sendMessage = async () => {
  isStoppedByUser.value = false; // 重置停止标志
  //避免重复提交
  if (ai_loading.value) {
    return;
  }
  //输入内容为空时不提交
  if (!user_input.value.trim()) return;

  //成功提交设置ai加载状态
  ai_loading.value = true;
  startTime.value = Date.now(); // 记录开始时间
  totalTokens.value = 0; // 重置token计数

  try {
    const prompt = user_input.value;
    user_input.value = "";
    ai_output.value = "";
    ai_outputList.value.push({ role: "user", content: prompt }); // 添加用户消息
    scrollToBottom();

    // 重置对话历史并添加系统提示词
    init_message.value = [SYSTEM_PROMPT, { role: "user", content: prompt }];

    // 如需提供局域网服务，请将请求地址替换为局域网地址 例如：http://192.168.3.20:8000/v1/chat/completions
    const response = await fetch("http://localhost:8000/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Authorization: "Bearer " + "key",
      },
      body: JSON.stringify({
        messages: init_message.value,
        max_tokens: 2048, // 最大生成长度
        temperature: 0.1, // 随机性
        use_search: isActiveSearch.value, // 启用用户搜索
        stream: true, // 启用流式请求
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
      // console.log("流数据：", chunk);

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
                totalTokens.value += content.length; // 累计token数量
                // 处理内容分割
                const newContent = ai_output.value + content;
                // 流式输出时不设置isCompleting
                const { thinking, answer, isThinkedAnswer } = processAIResponse(
                  newContent,
                  false
                );

                ai_output.value += content;
                ai_outputList.value[ai_outputList.value.length - 1].content +=
                  content;
                ai_outputList.value[ai_outputList.value.length - 1].content =
                  replaceMathSymbols(
                    ai_outputList.value[ai_outputList.value.length - 1].content
                  );

                // 更新最后一条消息
                // Proxy(Object) {AI_OutList: Proxy(Array)}
                const lastMsg =
                  ai_outputList.value[ai_outputList.value.length - 1];
                // console.log(lastMsg);
                lastMsg.thinking = thinking;
                lastMsg.answer = answer;
                lastMsg.isThinkedAnswer = isThinkedAnswer;

                scrollToBottom();
              }
            } catch (error) {
              console.error("解析 JSON 数据失败:", error, line);
            }
          } else {
            // 输出完成时的处理
            const { thinking, answer, isThinkedAnswer } = processAIResponse(
              ai_output.value,
              true
            );
            const lastMsg = ai_outputList.value[ai_outputList.value.length - 1];
            lastMsg.thinking = thinking;
            lastMsg.answer = answer;
            lastMsg.isThinkedAnswer = isThinkedAnswer;
            lastMsg.isCompleted = true;

            // 计算token速率
            const endTime = Date.now();
            const duration = (endTime - startTime.value) / 1000;
            lastMsg.tokenRate = Math.round(totalTokens.value / duration);

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
    const { thinking, answer, isThinkedAnswer } = processAIResponse(
      ai_output.value,
      true
    );
    // 更新最后一次消息
    // Proxy(Object) {AI_OutList: Proxy(Array)}
    const lastMsg = ai_outputList.value[ai_outputList.value.length - 1];
    lastMsg.thinking = thinking;
    lastMsg.answer = answer;
    lastMsg.isThinkedAnswer = isThinkedAnswer;
    if (!isStoppedByUser.value) {
      // 如果不是用户中止的,确保设置完成状态
      const lastMsg = ai_outputList.value[ai_outputList.value.length - 1];
      if (lastMsg && !lastMsg.isCompleted) {
        const endTime = Date.now();
        const duration = (endTime - startTime.value) / 1000;
        const tokenRate = Math.round(totalTokens.value / duration);

        lastMsg.isCompleted = true;
        lastMsg.tokenRate = tokenRate;
      }
    }
    ai_loading.value = false;
  }
};

//停止输出
const stopOutput = async () => {
  if (!ai_loading.value) return;

  isStoppedByUser.value = true; // 新增停止标志
  ai_loading.value = false;

  // 计算中止时的token速率
  const endTime = Date.now();
  const duration = (endTime - startTime.value) / 1000;
  const tokenRate = Math.round(totalTokens.value / duration);

  // 更新最后一条消息的状态
  const lastMsg = ai_outputList.value[ai_outputList.value.length - 1];
  lastMsg.isCompleted = true;
  lastMsg.tokenRate = tokenRate;

  await fetch("http://localhost:8000/api/stop_generation", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ confirm: true }),
  });
};

// 添加开启新对话方法
const startNewChat = () => {
  ai_outputList.value = [];
  init_message.value = [];
  ai_output.value = "";
  isStoppedByUser.value = false;
  totalTokens.value = 0;
};
</script>

<style scoped>
.app-container {
  display: flex;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.chat-container {
  flex: 1;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 0 20px; /* 添加左右内边距 */
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.logo {
  margin-right: 10px;
  color: #409eff;
}

.title {
  margin: 0;
  font-size: 24px;
}

.chat-content {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.message {
  margin: 15px 0;
}

.message-content {
  display: flex;
}

.user-message {
  justify-content: flex-end;
}

.user-message .message-content {
  flex-direction: row-reverse;
}

.bot-message .message-icon {
  color: #409eff;
  margin-right: 10px;
}

.user-message .message-icon {
  color: #67c23a;
  margin-left: 10px;
}

.text {
  background: #f5f7fa;
  padding: 12px 16px;
  border-radius: 8px;
  line-height: 1.6;
}

.user-message .text {
  background: #409eff;
  color: white;
}

.timestamp {
  font-size: 12px;
  color: #fff;
  margin-top: 4px;
}

.input-area {
  height: 92px;
  border-top: 1px solid #eee;
  padding: 10px;
  background-color: var(--dsr-input-bg);
  box-shadow: 0px 0px 0px 0.5px var(--dsr-input-border);
  border-radius: 24px;
}

:deep(.el-textarea) {
  border: none;
}

:deep(.input-area .el-textarea__inner) {
  resize: none;
  color: var(--ds-input-chat-color);
  caret-color: var(--ds-input-chat-color);
  background-color: transparent;
  border: none;
  outline: none; /* 移除聚焦时的边框 */
  box-shadow: none; /* 移除聚焦时的阴影 */
}

.input-container {
  margin: 4px 0;
}

/* 隐藏可能的边框选中效果 */
:deep(.chat-input .el-textarea__inner::selection) {
  background: transparent; /* 将选中背景设置为透明 */
}

.btn-area,
.ds-button {
  display: flex;
}

.ds-button {
  border: 1px solid rgba(8, 8, 8, 0.15);
  border-radius: 14px;
  justify-content: center;
  align-items: center;
  height: 26px;
  margin-right: 10px;
  padding: 0 7px;
  display: flex;
  cursor: pointer;
}

.ds-button .ds-button__icon {
  margin-right: 4px;
}

.ds-button:hover {
  background: rgba(0, 122, 255, 0.05);
}

.ds-button__enable {
  border: 1px solid rgba(0, 122, 255, 0.15);
  background: rgba(0, 122, 255, 0.15);
  color: #2563eb;
}

.ds-button__icon {
  display: flex;
  justify-content: center;
  height: 18px;
  width: 18px;
}

.ds-button__text {
  font-size: 11px;
  line-height: 19px;
}

.ds-button__icon svg {
  height: 17px;
  width: 17px;
}

.mgr-10 {
  margin-right: 10px;
}

.ds-button-area {
  flex: 1;
  justify-content: flex-end;
  align-items: center;
  display: flex;
}

.send-area {
  white-space: nowrap;
  cursor: pointer;
  color: #fff;
  background: #4d6bfe;
  border: none;
  border-radius: 6px;
  flex-direction: column;
  flex-shrink: 0;
  justify-content: center;
  align-items: center;
  min-width: 32px;
  height: 32px;
  margin-top: auto;
  display: flex;
}

.send-area:hover {
  background: #2563eb;
}

.send-btn {
  height: auto;
}

.mode-selector {
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
}

.ds-icon-stop {
  width: 12px;
  height: 12px;
  background: rgb(252, 250, 250);
}

.tip_msg {
  font-size: 12px;
  color: rgb(163, 163, 163);
  margin: 6px 0;
  line-height: 14px;
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

@media (max-width: 768px) {
  .chat-container {
    padding: 0 10px;
    max-width: 100%; /* 在小屏幕上占满宽度 */
  }

  .message-content {
    max-width: 90%;
  }
}

/* 新对话按钮样式 */
.new-chat-button {
  margin: 20px auto;
  cursor: pointer;
  width: fit-content;
}

.new-chat-content {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgb(219,234,254);
  border-radius: 20px;
  color: #4d6bfe;
  transition: all 0.2s ease;
}

.new-chat-content:hover {
  background: rgba(0, 122, 255, 0.25);
  
}

.new-chat-content svg {
  width: 18px;
  height: 18px;
}

.new-chat-content span {
  font-size: 14px;
}
</style>