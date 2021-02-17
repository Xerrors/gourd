<template>
  <div class="zhuanlan-container">
    {{ data }}
  </div>
</template>

<script>
import { defineComponent, ref, reactive } from 'vue';
import { getQueryVariable } from '../../utils/common';

import axios from 'axios';
export default {
  setup() {
    const name = getQueryVariable('name');

    function getDetails() {
      new Promise((resolve, reject) => {
        axios({
          url: "http://116.62.110.131:5000/zhuanlan",
          params: {
            name: name,
          }
        })
        .then(res => {
          console.log(res.data.data);
          data.value = res.data.data;
        })
      })
    }

    const data = ref({});

    

    return {
      data
    }
  }
}
</script>