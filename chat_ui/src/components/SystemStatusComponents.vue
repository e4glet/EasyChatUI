<template>
  <div class="system-status">
    <el-alert
      v-if="error"
      :title="error"
      type="error"
      show-icon
      :closable="false"
      class="mb-20"
    />
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card :body-style="{ position: 'relative' }">
          <template #header>
            <div class="card-header">
              <div class="title">CPU使用率</div>
              <div class="usage-detail">{{ formatNumber(systemStatus.cpu_usage) }}%</div>
            </div>
          </template>
          <el-progress 
            type="dashboard" 
            :percentage="formatNumber(systemStatus.cpu_usage)" 
            :color="getColorStatus"
            :stroke-width="6"
            :width="100"
          />          
          <el-loading v-if="loading" :value="loading" />
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <template #header>
            <div class="card-header">
              <div class="title">内存使用率</div>
              <div class="usage-detail">{{ systemStatus.memory_used }}/{{ systemStatus.memory_total }}GB</div>
            </div>
          </template>
          <el-progress 
            type="dashboard" 
            :percentage="memoryPercentage" 
            :color="getColorStatus"
            :stroke-width="6"
            :width="100"
          />
        </el-card>
      </el-col>
      <el-col :span="8" v-if="hasGPU">
        <el-card>
          <template #header>
            <div class="card-header">
              <div class="title">GPU显存</div>
              <div class="usage-detail">{{ systemStatus.gpu_memory_used }}/{{ systemStatus.gpu_memory_total }}GB</div>
            </div>
          </template>
          <el-progress 
            type="dashboard" 
            :percentage="gpuMemoryPercentage" 
            :color="getColorStatus"
            :stroke-width="6"
            :width="100"
          />
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const systemStatus = ref({
  cpu_usage: '0.0',
  memory_used: '0',
  memory_total: '0',
  gpu_memory_used: '0',
  gpu_memory_total: '0'
})
const loading = ref(false)
const error = ref('')

// 格式化数字，保留一位小数
const formatNumber = (num) => {
  return Number(num).toFixed(1)
}

const hasGPU = computed(() => 
  systemStatus.value.gpu_memory_total && Number(systemStatus.value.gpu_memory_total) > 0
)

const memoryPercentage = computed(() => {
  return Math.round((Number(systemStatus.value.memory_used) / Number(systemStatus.value.memory_total)) * 100)
})

const gpuMemoryPercentage = computed(() => {
  return Math.round((Number(systemStatus.value.gpu_memory_used) / Number(systemStatus.value.gpu_memory_total)) * 100)
})

// 颜色状态函数
const getColorStatus = (percentage) => {
  if (percentage < 60) return '#67C23A'
  if (percentage < 80) return '#E6A23C'
  return '#F56C6C'
}

// 更新获取系统状态的函数
const fetchSystemStatus = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await fetch('http://localhost:8000/api/system_info')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    systemStatus.value = data
  } catch (err) {
    error.value = '获取系统状态失败: ' + err.message
    console.error('获取系统状态失败:', err)
  } finally {
    loading.value = false
  }
}

let timer = null

onMounted(() => {
  fetchSystemStatus()
  timer = setInterval(fetchSystemStatus, 5000)
})

onBeforeUnmount(() => {
  if (timer) {
    clearInterval(timer)
  }
})
</script>

<style scoped>
.system-status {
  padding: 8px;
}
.card-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 13px;
  font-weight: bold;
  height: 42px;  /* 固定高度 */
  box-sizing: border-box;
}
.el-progress {
  display: flex;
  justify-content: center;
  margin: 8px 0;
}
.usage-detail {
  font-size: 10px;
  color: #909399;
  margin-top: 1px;
}

.card-header {
  text-align: center;
}

.mb-20 {
  margin-bottom: 8px;
}

.usage-value {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 12px);
  font-size: 11px;
  color: #606266;
}

.el-card {
  height: 100%;
  margin-bottom: 8px;
}

:deep(.el-card__header) {
  padding: 0;
  min-height: 40px;
}

:deep(.el-card__body) {
  padding: 6px;
}

:deep(.el-loading-mask) {
  background-color: rgba(255, 255, 255, 0.6);
}

:deep(.el-row) {
  margin: 0 !important;
}

:deep(.el-col) {
  padding: 0 6px !important;
}

:deep(.el-progress__text) {
  font-size: 12px !important;
}

:deep(.el-card) {
  --el-card-border-radius: 4px;
}

.title {
  margin-bottom: 2px;
}
</style>
