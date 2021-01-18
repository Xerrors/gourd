<template>
  <div class="message-container">
    <div class="button-list">
      <div class="platforms">
        <div v-for="(text, ind) in btn_text" :key=ind
           :class="{isSelected: ind === selected}">
          {{ text }}
        </div>
      </div>
      <button class="m-btn" @click="data.getMsgs">
        刷新
      </button>
    </div>
    <div class="msg-lists">
      <div :class="{msg: true, readed_msg: msg.readed}" v-for="(msg, ind) in data.msgs" :key=ind>
        <span class="msg__icon">{{ msg.id }}</span>
        <span class="msg__time">{{ msg.date }}</span>
        <a class="msg__text" :href="msg.link" @click="data.markAsReaded(msg.id)">{{ msg.content }}</a>
        <a-button type="link" class="msg-mark" @click="data.markAsReaded(msg.id)" :disabled="msg.readed">标记已读</a-button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { reactive, ref, resolveComponent } from "vue";
import request from '../utils/request';
import { message } from 'ant-design-vue';
import { parseTime } from '../utils/format';
export default {
  setup() {
    const btn_text = ref(["总览", "本站", "微信", "知乎", "掘金"]);
    const selected = ref(0);

    const parseMsg = (item:any):any => {
      item.date = parseTime(new Date(item.date))
      return item
    }

    const data = reactive({
      msgs: [],
      source: 'db',
      loading: false,
      getMsgs: () => {
        data.loading = true;
        new Promise((resolve, reject) => {
          request({
            url: '/api/admin/messages',
            method: 'get',
            params: {
              source: data.source,
            },
          })
          .then(res => {
            data.msgs = res.data.data.map(item => parseMsg(item));
            data.loading = false;
            resolve(res);
          })
          .catch(err => {
            data.loading = false;
            message.error(err.message);
            reject(err)
          })
        })
      },
      markAsReaded: (id) => {
        new Promise((resolve, reject) => {
          request({
            url: '/api/admin/readmessage',
            method: 'post',
            params: {
              id: id
            }
          })
          .then(res => {
            data.msgs = res.data.data.map(item => parseMsg(item));
            resolve(res);
          })
        })
      }
    })

    data.getMsgs()

    return {
      data,
      selected,
      btn_text,
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
      grid-template-columns: 24px 170px auto 100px;
      grid-gap: 24px;

      & > span, & > a {
        height: 20px;
        margin: 4px 0;

        font-size: 14px;
        // border: 1px dashed #333;
      }

      // &__time { color: #1d1d1d; }

      &__text {
        color: #222;
        overflow: hidden;
      }

      .msg-mark {
        color: #2F74DB;
      }
    }

    .readed_msg {
      background: rgba(255, 255, 255, 0.4);

      .msg__time, .msg__text { color: #888; }

      .msg-mark { color: gray; }
    }
  }
}
</style>