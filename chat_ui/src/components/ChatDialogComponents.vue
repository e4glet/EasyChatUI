<template>
  <div class="chat-item">
    <div
      class="chat-list"
      v-for="(message, index) in messageList"
      :key="index"
    >
      <div
        :class="[
          'chat-dialog',
          message.role === 'user' ? 'user-message' : 'ai-message',
        ]"
      >
        <template v-if="message.role === 'user'">
          {{ message.content }}
        </template>
        <template v-else>
          <!-- 思考过程容器 -->
          <div v-if="message.thinking" class="thinking-container">
            <div class="thinking-header">
              <div class="ds-icon">
                <svg
                  width="12"
                  height="12"
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
              <div>
                深度思考
                <span v-if="message.isStopped">已中止</span>
                <span v-else>
                  <span v-if="!message.answer">进行中</span>
                  <span v-else>已完成</span>
                </span>
              </div>
            </div>
            <div class="thinking-content">
              <div class="thinking-line"></div>
              {{ message.thinking }}
            </div>
          </div>

          <!-- 正式回答 -->
          <div v-if="message.answer" class="answer-container">
            <MdPreview
              v-model="message.answer"
              :preview-only="true"
              ref="mdPreview"
            />
            <!-- 添加底部信息栏,只在输出完成后显示 -->
            <div v-if="message.isCompleted" class="answer-footer">
              <div class="token-info">
                速率: {{ message.tokenRate || '0' }} tokens/s
              </div>
              <div 
                class="copy-button" 
                @click="copyAnswer(message.answer)"
                :class="{ 'copied': copiedMap[index] }"
              >
                <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                  <defs>
                    <clipPath id="clip1248_20193">
                      <rect width="17.052675" height="17.052441" transform="translate(1.000000 1.000000)" fill="white" fill-opacity="0"/>
                    </clipPath>
                    <clipPath id="clip1257_20794">
                      <rect width="20.000000" height="20.000000" fill="white" fill-opacity="0"/>
                    </clipPath>
                  </defs>
                  <g clip-path="url(#clip1257_20794)">
                    <g clip-path="url(#clip1248_20193)">
                      <path d="M5.03 14.64C4.77 14.64 4.5 14.62 4.24 14.56C3.98 14.51 3.73 14.43 3.49 14.33C3.24 14.23 3.01 14.1 2.79 13.96C2.57 13.81 2.37 13.64 2.18 13.45C1.99 13.26 1.82 13.05 1.68 12.83C1.53 12.61 1.4 12.37 1.3 12.13C1.2 11.88 1.13 11.63 1.07 11.36C1.02 11.1 1 10.84 1 10.57L1 5.07C1 4.8 1.02 4.54 1.07 4.27C1.13 4.01 1.2 3.76 1.3 3.51C1.4 3.26 1.53 3.03 1.68 2.81C1.82 2.58 1.99 2.38 2.18 2.19C2.37 2 2.57 1.83 2.79 1.68C3.01 1.53 3.24 1.41 3.49 1.31C3.73 1.2 3.98 1.13 4.24 1.07C4.5 1.02 4.77 1 5.03 1L10.49 1C10.75 1 11.01 1.02 11.27 1.07C11.53 1.13 11.78 1.2 12.03 1.31C12.27 1.41 12.51 1.53 12.73 1.68C12.95 1.83 13.15 2 13.34 2.19C13.53 2.38 13.69 2.58 13.84 2.81C13.99 3.03 14.11 3.26 14.21 3.51C14.31 3.76 14.39 4.01 14.44 4.27C14.5 4.54 14.52 4.8 14.52 5.07L12.94 5.07C12.94 4.91 12.92 4.75 12.89 4.58C12.86 4.43 12.81 4.27 12.75 4.12C12.69 3.97 12.61 3.83 12.52 3.69C12.43 3.56 12.33 3.43 12.22 3.32C12.1 3.2 11.98 3.1 11.85 3.01C11.71 2.92 11.57 2.84 11.42 2.78C11.27 2.72 11.12 2.67 10.96 2.64C10.81 2.61 10.65 2.59 10.49 2.59L5.03 2.59C4.87 2.59 4.71 2.61 4.55 2.64C4.4 2.67 4.24 2.72 4.09 2.78C3.95 2.84 3.8 2.92 3.67 3.01C3.54 3.1 3.41 3.2 3.3 3.32C3.18 3.43 3.08 3.56 2.99 3.69C2.9 3.83 2.83 3.97 2.77 4.12C2.71 4.27 2.66 4.43 2.63 4.58C2.6 4.75 2.58 4.91 2.58 5.07L2.58 10.57C2.58 10.73 2.6 10.89 2.63 11.05C2.66 11.21 2.71 11.37 2.77 11.52C2.83 11.67 2.9 11.81 2.99 11.94C3.08 12.08 3.18 12.2 3.3 12.32C3.41 12.43 3.54 12.54 3.67 12.63C3.8 12.72 3.95 12.79 4.09 12.86C4.24 12.92 4.4 12.96 4.55 13C4.71 13.03 4.87 13.04 5.03 13.04L5.03 14.64Z" fill="currentColor"/>
                    </g>
                    <path d="M14.75 18.91L9.3 18.91C9.03 18.91 8.77 18.88 8.51 18.83C8.25 18.78 8 18.7 7.75 18.6C7.51 18.49 7.27 18.37 7.05 18.22C6.83 18.07 6.63 17.9 6.44 17.71C6.25 17.52 6.09 17.32 5.94 17.1C5.79 16.87 5.67 16.64 5.57 16.39C5.47 16.14 5.39 15.89 5.34 15.63C5.28 15.37 5.26 15.1 5.26 14.83L5.26 9.33C5.26 9.06 5.28 8.8 5.34 8.54C5.39 8.28 5.47 8.02 5.57 7.77C5.67 7.53 5.79 7.29 5.94 7.07C6.09 6.85 6.25 6.64 6.44 6.45C6.63 6.26 6.83 6.09 7.05 5.95C7.27 5.8 7.51 5.67 7.75 5.57C8 5.47 8.25 5.39 8.51 5.34C8.77 5.29 9.03 5.26 9.3 5.26L14.75 5.26C15.01 5.26 15.28 5.29 15.54 5.34C15.8 5.39 16.05 5.47 16.29 5.57C16.54 5.67 16.77 5.8 16.99 5.95C17.21 6.09 17.41 6.26 17.6 6.45C17.79 6.64 17.96 6.85 18.1 7.07C18.25 7.29 18.37 7.53 18.48 7.77C18.58 8.02 18.65 8.28 18.71 8.54C18.76 8.8 18.78 9.06 18.78 9.33L18.78 14.83C18.78 15.1 18.76 15.37 18.71 15.63C18.65 15.89 18.58 16.14 18.48 16.39C18.37 16.64 18.25 16.87 18.1 17.1C17.96 17.32 17.79 17.52 17.6 17.71C17.41 17.9 17.21 18.07 16.99 18.22C16.77 18.37 16.54 18.49 16.29 18.6C16.05 18.7 15.8 18.78 15.54 18.83C15.28 18.88 15.01 18.91 14.75 18.91Z" fill="currentColor"/>
                  </g>
                </svg>
                <span>{{ copiedMap[index] ? '已复制' : '复制' }}</span>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { MdPreview } from "md-editor-v3";
import { ref, watch, nextTick, computed } from "vue";
import "md-editor-v3/lib/preview.css";

const props = defineProps({
  AI_OutList: {
    type: Array,
    required: true,
    default: () => [],
  },
  AI_StopByUser: Boolean,
});

// 使用计算属性来处理消息列表
const messageList = computed(() => {
  return props.AI_OutList.map(msg => {
    if (msg.role === 'assistant' && props.AI_StopByUser) {
      return {
        ...msg,
        isStopped: true
      }
    }
    return msg;
  });
});

const previewTheme = ref("default");

// 添加复制状态管理
const copiedMap = ref({});

// 复制功能
const copyAnswer = async (text) => {
  try {
    await navigator.clipboard.writeText(text);
    // 获取当前消息的索引
    const index = messageList.value.findIndex(msg => msg.answer === text);
    copiedMap.value[index] = true;
    
    // 2秒后重置复制状态
    setTimeout(() => {
      copiedMap.value[index] = false;
    }, 2000);
  } catch (err) {
    console.error('复制失败:', err);
  }
};

</script>

<style scoped>
.chat-item {
  width: 100%;
  display: flex;
  flex-direction: column; /* 子元素垂直排列 */
}

:deep(.v-note-wrapper) {
  min-height: 60px;
}

.chat-list {
  display: flex;
  flex-direction: column; /* 子元素垂直排列 */
  align-items: flex-end; /* 让聊天项靠右对齐 */
  width: 100%;
}

.user-message {
  display: flex;
  justify-content: flex-end; /* 保持靠右 */
  max-width: 60%; /* 限制最大宽度为60% */
  min-width: 0; /* 允许内容宽度小于容器宽度 */
  font-size: 14px;
  padding: 4px 8px;
  border-radius: 8px;
  background-color: #3d65f7;
  color: #ffffff;
  margin-bottom: 10px;
  word-wrap: break-word; /* 允许内容在达到最大宽度时换行 */
  overflow-wrap: break-word; /* 允许在长单词或URL内部进行换行 */
}

.ai-message {
  width: calc(100% - 6px);
  font-size: 14px;
  background-color: #f0f0f0;
  padding: 2px;
  border-radius: 6px;
  margin-bottom: 10px;
  text-align: left;
  word-wrap: break-word; /* 允许内容在达到最大宽度时换行 */
  overflow-wrap: break-word; /* 允许在长单词或URL内部进行换行 */
  align-self: flex-start; /* 让AI消息靠左对齐 */
}

/* 设置AI输出字体大小  */
:deep(.md-editor-preview) {
  font-size: 14px;
}

.loading {
  padding: 10px;
  color: #666;
  font-style: italic;
}

.markdown-preview {
  width: 100%;
  overflow: hidden;
  min-height: 20px;
}

.markdown-preview :deep(.md-editor-preview) {
  padding: 8px;
  background: transparent;
  font-size: 14px;
  line-height: 1.6;
}

/* 优化代码块显示 */
:deep(.md-editor-preview pre) {
  background-color: #f8f8f8 !important;
  border-radius: 6px;
  padding: 12px;
  margin: 8px 0;
}

/* 优化链接样式 */
:deep(.md-editor-preview a) {
  color: #3d65f7;
  text-decoration: none;
}

:deep(.md-editor-preview a:hover) {
  text-decoration: underline;
}

/* 优化表格样式 */
:deep(.md-editor-preview table) {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0;
}

:deep(.md-editor-preview th),
:deep(.md-editor-preview td) {
  border: 1px solid #ddd;
  padding: 8px;
}

:deep(.md-editor-preview-wrapper) {
  background: transparent !important;
}

/* 思考过程样式 */
.thinking-container {
  display: flex;
  flex-direction: column;
  background: #fff;
  border-radius: 6px 6px 0 0;
  padding: 8px;
}

.thinking-header {
  display: flex;
  width: fit-content;
  font-size: 12px;
  line-height: 12px;
  color: rgb(38, 38, 38);
  font-weight: 500;
  margin-bottom: 8px;
  background: rgb(245, 245, 245);
  padding: 7px 14px;
  border-radius: 10px;
}

.thinking-header .ds-icon {
  font-size: 12px;
  width: 12px;
  height: 12px;
  margin: 0 4px;
}

.thinking-content {
  font-size: 12px;
  color: #8b8b8b;
  white-space: pre-wrap;
  margin: 0;
  padding: 0 0 0 13px;
  line-height: 26px;
  position: relative;
}

.thinking-line {
  border-left: 2px solid #3d65f7;
  height: calc(100% - 10px);
  margin-top: 5px;
  position: absolute;
  top: 0;
  left: 0;
}

:deep(.md-editor-preview blockquote[data-line="0"]) {
  display: none;
}

/* 添加回答容器样式 */
.answer-container {
  position: relative;
}

/* 添加底部信息栏样式 */
.answer-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  margin-top: 8px;
  border-top: 1px solid #eee;
}

.token-info {
  font-size: 12px;
  color: #999;
}

.copy-button {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  border-radius: 4px;
  cursor: pointer;
  color: #666;
  font-size: 12px;
  transition: all 0.2s;
}

.copy-button:hover {
  background-color: #f5f5f5;
}

.copy-button.copied {
  color: #3d65f7;
}

.copy-button svg {
  width: 14px;
  height: 14px;
}

.copy-button.copied svg {
  color: #3d65f7;
}
</style>