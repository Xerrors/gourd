import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "HelloWorld",
    component: () => import("/@/views/HelloWorld.vue"),
  },
  {
    path: "/dashboard",
    name: "Home",
    component: () => import("/@/views/Home.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("/@/views/Login.vue"),
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});