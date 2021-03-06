<template>
  <div class="zhuanlan-container">
    <div class="zl-header">
      <div class="zl-header__img">
        <img :src="data.cover" alt="封面">
      </div>
      <div class="zl-header__info">
        <h3>{{ data.title }}</h3>
        <span>{{ data.date }}</span>
        <p>{{ data.description }}</p>
      </div>
    </div>
    <div>
      <div class="zl-body">
        <div class="zl-body__header">
          <span :class="{'active': show=='menu'}" @click="show='menu'">目录</span>
          <span :class="{'active': show=='details'}" @click="show='details'">介绍</span>
          <div v-if="show=='menu'">
            <button v-if="btn.order=='descend'" @click="btn.reversePages('ascend')"><CaretUpOutlined />降序</button>
            <button v-if="btn.order=='ascend'" @click="btn.reversePages('descend')"><CaretDownOutlined />升序</button>
          </div>
        </div>
        <div class="zl-body__container zl-body__menus" v-if="show=='menu'">
          <div class="zl-item" v-for="(page, ind) in localPages" :key="ind">
            <div class="zl-item__info">
              <h3 @click="goToPage(page.regularPath)">{{ page.frontMatter.title }}</h3>
              <span>{{ page.frontMatter.formattedDate }}</span>
            </div>
            <div class="zl-item__image" @click="goToPage(page.regularPath)">
              <img :src="page.frontMatter.cover + '?x-oss-process=image/resize,m_fill,h_180,w_340'" alt="">
            </div>
          </div>
        </div>
        <div class="zl-body__container zl-body__details" v-else>
          <pre>{{ data.details }}</pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, reactive } from 'vue';
import { useSiteDataByRoute, useRouter } from 'vitepress';
import { getQueryVariable } from '../../utils/common';
import { parseTime } from '../../utils/format';
import { CaretUpOutlined, CaretDownOutlined } from '@ant-design/icons-vue';

import axios from 'axios';
export default defineComponent({
  name: "zhuanlan",
  components: {
    CaretUpOutlined,
    CaretDownOutlined,
  },
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
          data.value.date = parseTime(new Date(data.value.date));
        })
      })
    }

    function getZhualnItems() {
      var pages = useSiteDataByRoute().value.themeConfig.pages;
      pages = pages.filter(item => item.frontMatter.zhuanlan==name)
      return pages;
    }

    const data = ref({});
    const show = ref('menu');
    const localPages = ref(getZhualnItems());

    const btn = reactive({
      order: 'ascend',
      reversePages: (order) => {
        btn.order = order;
        localPages.value.reverse();
      }
    })

    const router = useRouter();
    const goToPage = (path) => {
      router.go(path)
    }

    getDetails();

    return {
      data,
      localPages,
      show,
      goToPage,
      btn,
    }
  }
})
</script>

<style lang="scss" scoped>
.zhuanlan-container {
  width: var(--page-width);
  margin: 0 auto;
  margin-top: var(--header-height);
}

.zl-header {
  display: flex;
  width: 100%;
  padding: 54px 0;
  margin-bottom: 16px;

  &__img {
    // overflow: hidden;
    border-radius: 4px;

    img {
      max-width: 240px;
      height: 320px;
      object-fit: cover;
      border-radius: 4px;
    }
  }

  &__info {
    width: auto;
    padding: 44px 64px 16px 90px;

    h3 {
      font-size: 28px;
      line-height: 40px;
      color: #1A1A26;
    }

    span {
      font-size: 16px;
      line-height: 24px;
      color: #41414E;
    }

    p {
      font-size: 16px;
      line-height: 24px;
      text-align: justify;
      color: #20202F;
    }
  }
}

.zl-body {

  &__header {
    width: 100%;
    padding: 16px 0;
    margin-bottom: 1rem;

    span {
      cursor: pointer;
      margin-right: 16px;
      padding: 0.5rem 0.25rem;
    }

    span.active {
      color: var(--c-brand);
      border-bottom: 2px solid var(--c-brand);
    }

    div {
      display: inline-block;
      float: right;

      button {
        cursor: pointer;
        background: none;
        border: none;
        outline: none;

        &:hover {
          color: var(--c-brand);
        }
      }
    }
  }

  &__details {
    pre {
      text-align: justify;
      white-space: pre-wrap;
      word-wrap: break-word;
    }
  }
}

.zl-item {
  display: flex;
  height: 180px;
  margin-bottom: 24px;
  border: 1px solid #F2F2F2;
  transition: all 0.3s ease-in-out;
  animation: slide-in-blurred-bottom 0.5s cubic-bezier(0.230, 1.000, 0.320, 1.000) both;

  &__image {
    overflow: hidden;
    min-width: 340px;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    & > img {
      transition: all 0.3s ease-in-out;
      object-fit: cover;
      width: 340px;
      height: 180px;
    }
  }

  &__info {
    width: 100%;
    padding: 0 24px;
    position: relative;
    transition: all 0.3s ease-in-out;

    h3 {
      color: #1A1A26;
      margin-top: 38px;
      font-weight: bold;
      font-size: 20px;
      line-height: 24px;
      cursor: pointer;
      max-height: 56px;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    span {
      position: absolute;
      bottom: 27px;
      color: #41414E;
    }
  }
}

.zl-item:hover {
  .zl-item__image {
    width: 320px;
    min-width: 320px;

    & > img {
      transform: scale(1.05);
    }
  }

  .zl-item__info {
    padding-right: 16px;
    padding-left: 32px;
  }
}
</style>