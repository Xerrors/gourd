<template>
  <layout/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Layout from './components/Layout.vue'

import "/@/styles/index.scss"

export default defineComponent({
  name: 'App',
  components: {
    Layout
  }
})
</script>

<style lang="scss" scoped>
</style>
