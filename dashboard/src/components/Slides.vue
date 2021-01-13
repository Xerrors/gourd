<template>
  <div class="slides">
    <div class="logo">
      XERRORS
    </div>

    <div class="button-panel">
      <router-link to="/dashboard"><DashboardOutlined />后台总览</router-link>
      <router-link to="/pages"><FileTextOutlined />文章管理</router-link>
      <router-link to="/messages"><CommentOutlined />消息管理</router-link>
      <router-link to="/server-monitor"><DatabaseOutlined />服务器</router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { DashboardOutlined, FileTextOutlined, CommentOutlined, DatabaseOutlined } from '@ant-design/icons-vue';

import { defineComponent } from 'vue'
export default defineComponent({
  components: {
    DashboardOutlined,
    FileTextOutlined,
    DatabaseOutlined,
    CommentOutlined,
  }
});
</script>

<style lang="scss" scoped>
.slides.round {
  width: calc(var(--slides-width) - 20px);
  height: calc(100vh - 40px);

  background: rgba(255, 255, 255, 0.8);
  border: 1px solid #FFFFFF;
  border-radius: 32px;
  margin: 20px;
  
  box-sizing: border-box;
  // backdrop-filter: blur(32px);

  box-shadow: 1px 0px 20px 8px rgba(0,0,0,0.05);
}

.slides {
  position: fixed;
  top: 0;
  
  width: var(--slides-width);
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: center;

  background: white;
  
  .logo, .button-panel {
    width: 200px;
  }

  .logo {
    display: flex;
    justify-content: center;
    
    font-size: 28px;
    font-weight: bold;
    color: black;

    margin-top: 70px;
    height: 50px;
  }

  .button-panel {
    display: flex;
    flex-direction: column;
    align-items: center;

    height: auto;

    margin-top: 50px;

    a {
      display: flex;
      align-items: center;
      gap: 8px;

      border-radius: 8px;
      margin: 24px;
      padding: 8px 28px;

      color: black;
      font-weight: bold;
      text-decoration: none;

      letter-spacing: 2px;

      font-size: 16px;
      line-height: 24px;

      transition: background .2s ease-in-out;

      &:hover:not(.router-link-active) {
        background: #edf8ff;
      }
    }

    .router-link-active {
      background: black;
      color: white;
    }
  }
}
</style>
