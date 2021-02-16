// import DefaultTheme from 'vitepress/theme';
import DefaultTheme from "../theme-default";
// import IconifyIcon from '@iconify/vue';

import './styles/index.css';

// import Antd from 'ant-design-vue';
// import 'ant-design-vue/dist/antd.css';

import Loading from "./components/Loading.vue";
import Comment from "./components/Comment.vue";
import BlogPage from "./components/BlogPage.vue";
import HomePage from "./components/HomePage.vue";
import ZonePage from "./components/ZonePage.vue";
import AboutPage from "./components/AboutPage.vue";
import FriendPage from "./components/FriendPage.vue";

const myTheme = { ...DefaultTheme, Layout: { ...DefaultTheme.Layout } }

export default {
  ...myTheme,
  NotFound: () => 'custom 404',
  enhanceApp({ app, router, siteData }) {
    
    // 注册组件
    // app.use(Antd);
    // app.component("IconifyIcon", IconifyIcon);
    app.component("Comment", Comment);
    app.component("HomePage", HomePage);
    app.component("BlogPage", BlogPage);
    app.component("ZonePage", ZonePage);
    app.component("AboutPage", AboutPage);
    app.component("FriendPage", FriendPage);
    app.component("Loading", Loading);

    // app is the Vue 3 app instance from createApp()
    // router is VitePress' custom router (see `lib/app/router.js`)
    // siteData is a ref of current site-level metadata.
  },
};