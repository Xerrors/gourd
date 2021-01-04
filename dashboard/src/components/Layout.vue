<template>
  <div class="default-container">
    <slides/>

    <main>
      <navbar></navbar>
      <router-view/>
    </main>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import Slides from './Slides.vue'
import Navbar from './Navbar.vue'

export default defineComponent({
  name: 'Layout',
  components: {
    Slides,
    Navbar,
  }
})
</script>

<style lang="scss" scoped>
  .default-container {

    background: linear-gradient(124.51deg, #EBF8FF 11.89%, #e5f1ff 86.3%);

    main{
      margin-left: var(--slides-width);
      min-height: 100vh;
      width: auto;

      padding: 0 24px;

      /* for test */
      height: 1000px;
    } 
  }
</style>