<template>
  <div class="slides">
    <div class="logo">
      LOGO
    </div>

    <div class="button-panel">
      <router-link to="/dashboard">后台总览</router-link>
      <router-link to="/pages">文章管理</router-link>
      <router-link to="/messages">消息管理</router-link>
      <router-link to="/server-monitor">服务器</router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.slides {
  position: fixed;
  top: 0;

  width: var(--slides-width);
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: center;

  background: white;
  border-radius: 0 32px 32px 0;

  background: rgba(255, 255, 255, 0.6);
  border: 1px solid #FFFFFF;
  box-sizing: border-box;
  backdrop-filter: blur(32px);

  box-shadow: 1px 0px 20px 8px rgba(0,0,0,0.05);
  
  .logo, .button-panel {
    width: 200px;
  }

  .logo {
    display: flex;
    justify-content: center;

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

      width: 100px;
      height: 36px;

      border-radius: 8px;
      margin: 24px;
      padding: 4px 28px;

      color: black;
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