<template>
  <div class="default-container">
    <slides/>

    <header>
      <navbar></navbar>
    </header>

    <main>
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