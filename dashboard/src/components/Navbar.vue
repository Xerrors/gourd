<template>
  <div class="navbar">
    <h1>{{ route_name }}</h1>
    <a-button type="primary" class="nav-btn" @click="routerJump('/edit/draft')">
      开始写作
    </a-button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, toRaw } from 'vue';
import { useRoute, useRouter } from "vue-router";
export default defineComponent({
  name: "navbar",
  setup() {
    let route = useRoute();
    let router = useRouter();
    let route_name = toRaw(route).name;

    const routerJump = (path:string):void => {
      router.push(path);
    }

    return {
      route_name,
      routerJump,
    }
  },
});
</script>

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