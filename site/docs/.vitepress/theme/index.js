import Antd from 'ant-design-vue';
import Layout from './Layout.vue'

import 'ant-design-vue/dist/antd.css';

export default {
  Layout,
  enhanceApp({ app, router, siteData }) {
    // 注册组件
    app.use(Antd);
    
    app.config.productionTip = false;

    // app is the Vue 3 app instance from createApp()
    // router is VitePress' custom router (see `lib/app/router.js`)
    // siteData is a ref of current site-level metadata.
  },
};