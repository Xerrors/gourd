<template>
  <div class="zhuanlan-container">
    {{ name }}
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { getQueryVariable } from '../../utils/common';
export default {
  setup() {
    const name = getQueryVariable('name');

    return {
      name
    }
  }
}
</script>