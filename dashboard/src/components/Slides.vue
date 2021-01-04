<template>
  <div class="slides">
    <div class="logo">
      LOGO
    </div>

    <div class="button-panel">
      <router-link to="/dashboard">后台总览</router-link>
      <router-link to="/">文章管理</router-link>
      <router-link to="/a">消息管理</router-link>
      <router-link to="/b">服务器</router-link>
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
      background: linear-gradient(124.51deg, #DA62C7 11.89%, #E147D2 86.3%);
      color: white;
    }
  }

}
</style>