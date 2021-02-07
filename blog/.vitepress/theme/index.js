import DefaultTheme from 'vitepress/theme'

// import Antd from 'ant-design-vue';
// import 'ant-design-vue/dist/antd.css';

import Comment from "./components/Comment.vue";
import Blog from "./components/Blog.vue";
import Home from "./components/Home.vue";


export default {
  ...DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    
    // 注册组件
    // app.use(Antd);
    app.component("Comment", Comment);
    app.component("Home", Home);
    app.component("Blog", Blog);

    // app is the Vue 3 app instance from createApp()
    // router is VitePress' custom router (see `lib/app/router.js`)
    // siteData is a ref of current site-level metadata.
  },
};