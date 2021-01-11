<template>
  <div class="navbar">
    <h1>后台总览</h1>
    <a-button type="primary" class="nav-btn">
      开始写作
    </a-button>
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

  h1 {
    font-size: 28px;
    font-weight: 600;
    line-height: 40px;
  }

  .nav-btn {
    margin-left: auto;
    border-radius: 4px;
  }
}
</style>