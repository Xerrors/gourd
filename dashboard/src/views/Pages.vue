<template>
  <div class="pages">
    <a-list
      class="demo-loadmore-list"
      :loading="data.loading"
      item-layout="horizontal"
      :data-source="data.filted_articles"
    >
      <template #header>
        <h2 class="header-title">
          共 {{ data.filted_articles.length }} 篇文章
        </h2>
        <a-date-picker :value="data.endDate" @change="data.onDateChange" />
        <a-select
          :value="data.source"
          style="width: 100px"
          ref="select"
          @change="data.getData"
          :loading="data.loading"
        >
          <a-select-option value=""> 本站 </a-select-option>
          <a-select-option value="csdn"> CSDN </a-select-option>
          <a-select-option value="zhihu"> 知乎 </a-select-option>
        </a-select>
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
            <a-popconfirm
              placement="left"
              title="编辑文章需要在对应平台登录，是否跳转？"
              ok-text="是的"
              cancel-text="取消"
              @confirm="onOpenNewPage(item.edit_link)"
              @cancel="onCancel"
            >
              <a :href="item.edit_link" target="_blank">编辑</a>
            </a-popconfirm>
            <a :href="item.link" target="_blank">查看</a>
            <a style="color: var(--error-color)">删除</a>
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
import { defineComponent, ref, reactive, computed } from "vue";

import request from "../utils/request";
import { parseTime, joinPath } from "../utils/format";

import { message } from "ant-design-vue";

export default defineComponent({
  name: "Pages",
  setup() {
    let data = reactive({
      source: "",
      articles: [],
      filted_articles: [],
      loading: false,
      endDate: "",

      filter_date: (item:any):boolean => { return true},

      onDateChange: (selectDate: Date, dateString: string) => {
        data.endDate = dateString;
        if (dateString) {
          data.filter_date = (item) => {
            return new Date(item.date) < new Date(dateString)
          };
        } else {
          data.filter_date = ():boolean => { return true};
        }
        data.filted_articles = data.articles.filter(data.filter_date);
      },

      getData: (source: string) => {
        data.loading = true;
        new Promise((resolve, reject): void => {
          request({
            url: "/api/articles",
            method: "get",
            params: { source: source },
          })
            .then((res) => {
              let articles = res.data.data.map((item:any) => {
                item.date = parseTime(new Date(item.date));
                if (source === "csdn") {
                  item.link =
                    "https://blog.csdn.net/jaykm" +
                    "/article/details/" +
                    item.article_id;
                  item.edit_link =
                    "https://editor.csdn.net/md/?articleId=" + item.article_id;
                } else {
                  item.link = joinPath(
                    "https://www.xerrors.fun/",
                    item.permalink
                  );
                }
                return item;
              });

              articles.sort((a:any, b:any) => {
                return Number(new Date(b.date)) - Number(new Date(a.date));
              });

              data.articles = articles;
              data.filted_articles = articles.filter(data.filter_date);
              data.loading = false;
              message.success("加载完成");
            })
            .catch((err) => {
              reject(err);
            });
        });
      },
    });

    // data.articles = context.getData(data.source);
    data.getData(data.source);

    return {
      data,
    };
  },
  methods: {
    onOpenNewPage(link: string): void {
      window.open(link);
    },

    onCancel() {
      message.error("取消跳转");
    },
  },
});
</script>

<style lang="scss">
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
// 未生效
.ant-popover-inner {
  backdrop-filter: blur(16px);
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid white;
  border-radius: 8px;
  box-shadow: 1px 1px 12px 2px rgba(0, 0, 0, 0.05);
}

.ant-select,
.ant-calendar-picker {
  margin-left: 20px;
  float: right;
}
</style>

<style lang="scss" scoped>
.pages {
  padding: 8px 20px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  box-shadow: 1px 1px 12px 2px rgba(0, 0, 0, 0.05);
}
</style>