import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import VueWechatTitle from 'vue-wechat-title'; //统一标题
import * as ElementPlusIconsVue from '@element-plus/icons-vue'; //引入elementPlus图标

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.use(store).use(router).use(ElementPlus).use(VueWechatTitle).mount('#app')
