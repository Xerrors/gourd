<template>
  <div class="message-container">
    <div class="button-list">
      <div class="platforms">
        <div v-for="(text, ind) in btn_text" :key=ind
           :class="{isSelected: ind === selected}">
          {{ text }}
        </div>
      </div>
      <button class="m-btn">
        刷新
      </button>
    </div>
    <div class="msg-lists">
      <div class="msg-card" v-for="(msg, ind) in msgs" :key=ind>
        {{ msg }}
        <button class="msg-view">查看</button>
        <button class="msg-delete">删除</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from "vue"
export default {
  setup() {
    const btn_text = ref(["总览", "本站", "微信", "知乎", "掘金"]);
    const msgs = ref(["1", "2", "3", "4"])
    const selected = ref(0);

    return {
      selected,
      btn_text,
      msgs,
    };
  }
}
</script>

<style lang="scss" scoped>
.message-container {
  .button-list, .msg-lists {
    width: 100%;
  }

  .button-list {
    display: flex;

    .platforms {
      display: flex;
      height: 44px;
      padding: 2px;

      border: 1px solid #FFFFFF;
      box-sizing: border-box;
      backdrop-filter: blur(32px);
      /* Note: backdrop-filter has minimal browser support */

      border-radius: 8px;

      & > div {
        width: 100px;
        border-radius: 8px;

        text-align: center;
        line-height: 40px;
        cursor: pointer;
      }

      .isSelected {
        background: white;
      }
    }

    button {
      margin: 2px;
      margin-left: 24px;
    }
  }

  .msg-lists {
    
    .msg-card {
      margin-top: 12px;
      padding: 12px 24px;

      background: rgba(255, 255, 255, 0.6);
      border: 1px solid #FFFFFF;
      box-sizing: border-box;
      box-shadow: 0px 2px 16px rgba(47, 116, 219, 0.05);
      backdrop-filter: blur(32px);
      /* Note: backdrop-filter has minimal browser support */

      border-radius: 8px;
    }
  }
}
</style>