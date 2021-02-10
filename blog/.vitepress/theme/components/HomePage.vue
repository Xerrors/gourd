<template>
  <div class="home-container">
    <div class="hero">
      <h1>{{ data.heroText }}</h1>
      <p>{{ data.description }}</p>
      <button class="action-btn" @click="action(data.actionLink)">
        {{ data.actionText }}
      </button>
      <img src="../asserts/img/home.svg" alt="" />
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useFrontmatter, useRouter } from "vitepress";
export default defineComponent({
  name: "Home",
  setup() {
    const data = useFrontmatter();
    const router = useRouter();

    const action = (path) => {
      router.go(path);
    }

    return {
      data,
      action,
    };
  },
});
</script>

<style lang="scss" scoped>
.home-container {
  max-width: var(--page-width-w);
  margin: 0 auto;
}

.hero {
  position: relative;
  height: 100vh;
  max-height: 1300px;
  padding-top: 200px;

  h1 {
    margin-top: 0;
    font-style: normal;
    font-weight: bold;
    font-size: 64px;
    line-height: 80px;
    color: #1A1A26;
  }

  p {
    font-style: normal;
    font-weight: 300;
    font-size: 18px;
    line-height: 40px;
    letter-spacing: 4px;
  }

  button {
    display: block;
    border: none;
    cursor: pointer;
    font-weight: bold;
    font-size: 18px;
    line-height: 26px;
    letter-spacing: 4px;
    color: white;
    padding: 8px 32px;
    background: #000000;
    border-radius: 4px;

    margin-top: 60px;

    &:hover {
      background-color: #1A1A26;
    }
  }

  img {
    width: 900px;
    height: 600px;
    position: absolute;
    right: 0;
    bottom: 0;
  }
}
</style>