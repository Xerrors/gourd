<template>
  <div class="pages">
    <a-list
      class="demo-loadmore-list"
      :loading="loading"
      item-layout="horizontal"
      :data-source="data.articles"
    >
      <template #header>
        <h2 class="header-title">共 {{ data.articles.length }} 篇文章 </h2>
        <!-- <a-date-picker :value="data.endDate" @change="data.onDateChange" /> -->
      </template>
      <template #renderItem="{ item, index }">
        <a-list-item>
          <span class="list-date">{{ item.date }}</span>
          <a-list-item-meta>
            <template #title>
              <a :href="item.link" target="_blank">{{ item.title }}</a>
            </template>
          </a-list-item-meta>
          <template #actions>
            <a>编辑</a>
            <a :href="item.link" target="_blank">查看</a>
            <a style="color: var(--error-color);">删除</a>
          </template>
        </a-list-item>
      </template>
      <!-- <template #loadMore>
        <div
          v-if="showLoadingMore"
          :style="{
            textAlign: 'center',
            marginTop: '12px',
            height: '32px',
            lineHeight: '32px',
          }"
        >
          <a-spin v-if="loadingMore" />
          <a-button v-else @click="onLoadMore"> loading more </a-button>
        </div>
      </template> -->
    </a-list>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from "vue";

import request from "../utils/request";
import { parseTime, joinPath } from "../utils/format";

export default defineComponent({
  name: "Pages",
  setup() {
    let loading = ref(false);

    let data = reactive({
      articles: [],
      // endDate: new Date(Date.now()),
      // onDateChange: (date:Date, dateString:string) => {
      //   data.endDate = date;
      //   console.log(dateString);
      // }
    });
    new Promise((resolve, reject): void => {
      request({ url: "/api/articles", method: "get" })
        .then((res) => {
          data.articles = res.data.data.map((item) => {
            item.date = parseTime(new Date(item.date));
            item.link = joinPath("https://www.xerrors.fun/", item.permaklink);
            return item;
          });
          data.articles.sort((a, b) => {
            return Number(new Date(b.date)) - Number(new Date(a.date));
          });
        })
        .catch((err) => {
          reject(err);
        });
    });

    return {
      data,
      loading,
    };
  },
});
</script>

<style lang="scss">
.pages {
  padding: 8px 20px;
  background: rgba(255,255,255,0.8);
  border-radius: 16px;
  box-shadow: 1px 1px 12px 2px rgba(0,0,0,0.05);

  .ant-list .header-title {
    display: inline-block;
  }

  .ant-list-item:hover {
    background: white;
  }

  .list-date {
    width: 150px;
  }

  .ant-list-item-meta-title {
    // color: rgba(0, 0, 0, 0.8);
    margin: 4px;
  }
}
</style>