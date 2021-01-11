import { createApp } from 'vue'
import App from './App.vue'

import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
// import './styles/my-theme-file.less' // 修改部分 antd 自带的样式

import "./styles/index.scss";

import router from "./router";
import store from "./store";

const app = createApp(App);

app.use(router);
app.use(store);
app.use(Antd);
app.mount('#app');