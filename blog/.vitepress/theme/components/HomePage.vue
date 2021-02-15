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
import axios from 'axios';
export default defineComponent({
  name: "Home",
  setup() {
    const data = useFrontmatter();
    const router = useRouter();

    const action = (path) => {
      router.go(path);
    }

    const viewCount = ref(0);

    new Promise((resolve, reject) => {
      axios({
        url: "http://116.62.110.131:5000/visit",
        method: 'get',
        params: {
          path: 'cycle-gan-reading-note',
          count: 'cycle-gan-reading-note'
        }
      })
      .then(res => {
        console.log(res.data.data);
        viewCount.value = res.data.data;
        resolve(res);
      })
      .catch(err => {
        resolve(err);
      })
    })

    return {
      data,
      action,
      viewCount,
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
  padding-top: calc(var(--header-height) + 2rem);

  h1 {
    margin-top: 0;
    font-style: normal;
    font-weight: bold;
    font-size: 3.25rem;
    line-height: 4rem;
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
    font-size: 1rem;
    line-height: 1.75rem;
    letter-spacing: 4px;
    color: white;
    padding: 8px 32px;
    background: #000000;
    border-radius: 8px;

    margin-top: 3rem;

    &:hover {
      background-color: #1A1A26;
    }
  }

  img {
    width: 900px;
    position: absolute;
    right: 0;
    bottom: 0;
  }
}
</style>