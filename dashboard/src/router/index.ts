import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "HelloWorld",
    component: () => import("../views/HelloWorld.vue"),
  },
  {
    path: "/dashboard",
    name: "后台总览",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/pages",
    name: "文章管理",
    component: () => import("../views/Pages.vue"),
  },
  {
    path: "/messages",
    name: "消息管理",
    component: () => import("../views/Messages.vue"),
  },
  {
    path: "/server-monitor",
    name: "服务器状态",
    component: () => import("../views/ServerMonitor.vue"),
  },
  {
    path: "/404",
    name: "404",
    component: () => import("../views/404.vue"),
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});