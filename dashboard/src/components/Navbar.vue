<template>
  <div class="navbar">
    <h1>预览</h1>
    <button class="m-btn nav-btn">开始写作</button>
  </div>
</template>

<style lang="scss" scoped>
.navbar {
  //position: sticky;
  top: 0;

  width: 100%;
  height: var(--navbar-height);

  display: flex;
  align-items: center;

  .nav-btn {
    margin-left: auto;
  }
}
</style>