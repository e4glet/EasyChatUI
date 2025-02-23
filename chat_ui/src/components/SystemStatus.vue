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
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card :body-style="{ position: 'relative' }">
          <template #header>
            <div class="card-header">
              <div class="title">CPU</div>
              <div class="usage-detail">{{ formatNumber(systemStatus.cpu_usage) }}%</div>
            </div>
          </template>
          <el-progress 
            type="dashboard" 
            :percentage="formatDisplayNumber(systemStatus.cpu_usage)" 
            :color="getColorStatus"
            :stroke-width="4"
            :width="60"
          />          
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <template #header>
            <div class="card-header">
              <div class="title">内存</div>
              <div class="usage-detail">{{ formatNumber(memoryPercentage) }}%</div>
            </div>
          </template>
          <el-progress 
            type="dashboard" 
            :percentage="Number(memoryPercentage)" 
            :color="getColorStatus"
            :stroke-width="4"
            :width="60"
          />
        </el-card>
      </el-col>
      <el-col :span="8" v-if="hasGPU">
        <el-card>
          <template #header>
            <div class="card-header">
              <div class="title">GPU</div>
              <div class="usage-detail">{{ formatNumber(gpuMemoryPercentage) }}%</div>
            </div>
          </template>
          <el-progress 
            type="dashboard" 
            :percentage="Number(gpuMemoryPercentage)" 
            :color="getColorStatus"
            :stroke-width="4"
            :width="60"
          />
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  enabled: {
    type: Boolean,
    default: false
  }
})

const systemStatus = ref({
  cpu_usage: 0,  // 改为数字类型初始值
  memory_used: 0,
  memory_total: 1, // 避免除以0
  gpu_memory_used: 0,
  gpu_memory_total: 1
})
const loading = ref(false)
const error = ref('')
let timer = null

// 安全的数值转换函数
const safeNumber = (value, defaultValue = 0) => {
  const num = Number(value)
  return isNaN(num) ? defaultValue : num
}

// 格式化显示用的数字
const formatNumber = (num) => {
  return safeNumber(num).toFixed(1)
}

// 确保返回有效的百分比数值
const formatDisplayNumber = (num) => {
  const value = safeNumber(num)
  return Math.min(Math.max(value, 0), 100) // 确保值在0-100之间
}

const hasGPU = computed(() => 
  systemStatus.value.gpu_memory_total && Number(systemStatus.value.gpu_memory_total) > 0
)

const memoryPercentage = computed(() => {
  const used = safeNumber(systemStatus.value.memory_used)
  const total = safeNumber(systemStatus.value.memory_total, 1) // 防止除以0
  return Math.round((used / total) * 100)
})

const gpuMemoryPercentage = computed(() => {
  const used = safeNumber(systemStatus.value.gpu_memory_used)
  const total = safeNumber(systemStatus.value.gpu_memory_total, 1)
  return Math.round((used / total) * 100)
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
    // console.log('获取系统状态成功:', data)
  } catch (err) {
    error.value = '获取系统状态失败: ' + err.message
    console.error('获取系统状态失败:', err)
  } finally {
    loading.value = false
  }
}

// 先定义轮询控制函数
const stopPolling = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const startPolling = () => {
  stopPolling() // 确保先清理
  timer = setInterval(fetchSystemStatus, 5000)
}

// 然后再定义 watch
watch(() => props.enabled, (newValue) => {
  if (newValue) {
    fetchSystemStatus()
    startPolling()
  } else {
    stopPolling()
  }
}, { immediate: true })

// 组件卸载时确保清理
onBeforeUnmount(() => {
  stopPolling()
})
</script>

<style scoped>
.system-status {
  padding: 4px;
}

.card-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 11px;
  font-weight: bold;
  height: 32px;
  box-sizing: border-box;
}

.el-progress {
  display: flex;
  justify-content: center;
  margin: 4px 0;
}

.usage-detail {
  font-size: 9px;
  color: #909399;
  margin-top: 1px;
}

.mb-20 {
  margin-bottom: 4px;
}

.el-card {
  height: 100%;
  margin-bottom: 4px;
}

:deep(.el-card__header) {
  padding: 0;
  min-height: 32px;
}

:deep(.el-card__body) {
  padding: 4px;
}

:deep(.el-row) {
  margin: 0 !important;
}

:deep(.el-col) {
  padding: 0 4px !important;
}

:deep(.el-progress__text) {
  font-size: 10px !important;
  font-weight: normal !important;
}

:deep(.el-card) {
  --el-card-border-radius: 3px;
  --el-card-border-color: #e4e7ed80;
  box-shadow: none !important;
}

.title {
  margin-bottom: 1px;
  font-size: 10px;
  color: #606266;
}

:deep(.el-progress) {
  --el-progress-text-font-size: 10px;
}
</style>
