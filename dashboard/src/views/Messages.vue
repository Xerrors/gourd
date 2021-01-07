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
      <div :class="{msg: true, 'readed_msg': msg.readed}" v-for="(msg, ind) in msgs" :key=ind>
        <span class="msg__icon">{{ msg.id }}</span>
        <span class="msg__time">{{ msg.time }}</span>
        <span class="msg__text">{{ msg.content }}</span>
        <button class="btn-text msg-view">查看</button>
        <button class="btn-text msg-delete">删除</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from "vue"
export default {
  setup() {
    const btn_text = ref(["总览", "本站", "微信", "知乎", "掘金"]);
    const msgs = ref([
    {
      id: 1,
      content:"消息标题", 
      readed: false,
      date: new Date(),
      url: "",
    }, {
      id: 2,
      content: "玉川在你的文章《青林紫竹风铃里》下评论了“英雄所见略同”", 
      readed: false,
      date: new Date(),
      url: "",
    }, {
      id: 3,
      content: "玉川在你的文章《青林紫竹风铃里》下评论了“英雄所见略同”", 
      readed: false,
      date: new Date(),
      url: "",
    }, {
      id: 4,
      content: "玉川在你的文章《青林紫竹风铃里》下评论了“英雄所见略同”", 
      readed: false,
      date: new Date(),
      url: "",
    }, {
      id: 5,
      content: "玉川在你的文章《青林紫竹风铃里》下评论了“英雄所见略同”", 
      readed: true,
      date: new Date(),
      url: "",
    }
    ])
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
      // backdrop-filter: blur(32px);
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
    
    .msg {
      margin-top: 12px;
      padding: 10px 24px;

      background: rgba(255, 255, 255, 0.6);
      border: 1px solid #FFFFFF;
      box-sizing: border-box;
      box-shadow: 0px 2px 16px rgba(47, 116, 219, 0.05);
      // backdrop-filter: blur(32px);
      /* Note: backdrop-filter has minimal browser support */

      border-radius: 8px;

      display: grid;
      grid-template-columns: 24px 170px auto 56px 56px;
      grid-gap: 24px;

      & > span {
        height: 20px;
        margin: 4px 0;

        font-size: 14px;
        // border: 1px dashed #333;
      }

      &__time {
        color: #1d1d1d;
      }

      &__text {
        color: #222;
      }

      .msg-view, .msg-delete {
        // height: 24px;
      }

      .msg-view {
        color: #2F74DB;
      }

      .msg-delete {
        color: #E31748;
      }
    }
  }
}
</style>