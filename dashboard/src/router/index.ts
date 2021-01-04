import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "HelloWorld",
    component: () => import("../views/HelloWorld.vue"),
  },
  {
    path: "/dashboard",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/pages",
    name: "Pages",
    component: () => import("../views/Pages.vue"),
  },
  {
    path: "/messages",
    name: "Messages",
    component: () => import("../views/Messages.vue"),
  },
  {
    path: "/server-monitor",
    name: "ServerMonitor",
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