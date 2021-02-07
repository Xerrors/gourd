<template>
  <div class="blog-container">
    <div class="slideshow">
      <img src="https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519142253.png" alt="轮播图">
    </div>

    <div class="categories">
      <span
        v-for="(cat, ind) in categories.labels"
        :key="ind"
        :class="{active: categories.active == cat}"
        @click="categories.selectCategory(cat)"
        >
        {{ cat }}
      </span>
    </div>

    <div class="search-box">
      搜索
    </div>

    <div class="blogs">
      <div
        class="blog-card"
        v-for="(page, ind) in filtedPages"
        :key="ind"
        >
        <div class="blog-card__image" @click="goToPage(page.regularPath)">
          <img :src="page.frontMatter.cover" alt="">
        </div>

        <div class="blog-card__info">
          <h3 @click="goToPage(page.regularPath)">{{ page.frontMatter.title }}</h3>
          <span>{{ page.frontMatter.formattedDate }}</span>
        </div>
      </div>
    </div>

    <div class="blog-right">

      <h4>我的专栏</h4>

      <div class="zhuanlan-slideshow">
        <img src="https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20201009130905.png" alt="">
      </div>

      <h4>标签查询</h4>

    </div>
  </div>
</template>

<script>
import { defineComponent, ref, reactive, computed } from 'vue';
import { useSiteDataByRoute, useRouter } from "vitepress";
import { formatTime } from "../../utils/format";

export default defineComponent({
  setup() {

    const categories = reactive({
      labels: ["全部", "前端", "人工智能", "算法", "基础"],
      active: "全部",
      selectCategory: (link) => {
        categories.active = link;
      }
    })

    let pages = useSiteDataByRoute().value.themeConfig.pages;
    let filtedPages = computed(() => {
      if (categories.active != "全部") {
        return pages.filter(item => {
          return item.frontMatter.categories === categories.active 
              || item.frontMatter.categories[0] === categories.active
        })
      } else {
        return pages;
      }
    })

    const router = useRouter();
    const goToPage = (path) => {
      router.go(path)
    }

    return {
      filtedPages,
      categories,
      goToPage,
    }
  }
})


</script>

<style lang="scss" scoped>
.blog-container {
  margin: 0 auto;
  margin-top: 80px;
  width: 1136px;

  display: grid;
  grid-template-columns: 9fr 3fr;
  grid-template-rows: 420px 60px auto;
  grid-column-gap: 30px;
  grid-row-gap: 20px;
}

.slideshow {
  width: 100%;
  border-radius: 4px;
  overflow: hidden;

  grid-column-start: span 2;

  img {
    object-fit: cover;
    width: 100%;
  }
}

.categories {
  height: 100%;
  padding-top: 12px;

  span {
    font-size: 20px;
    line-height: 24px;
    padding: 8px 20px;
    margin-right: 16px;
    cursor: pointer;
    transition: all 0.2s ease-in-out;

    &:not(.active):hover {
      background: #fafafa;
      border-radius: 4px;
    }
  }

  .active {
    font-weight: Bold;
    color: #e63657;
    padding: 12px 20px;

    border-bottom: 4px solid #E63657;
  }
}

.blogs {
  .blog-card {
    display: flex;
    height: 180px;
    margin-bottom: 24px;
    border: 1px solid #F2F2F2;
    transition: all 0.3s ease-in-out;

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
      }

      span {
        position: absolute;
        bottom: 27px;
        color: #41414E;
      }
    }
  }

  .blog-card:hover {
    .blog-card__image {
      width: 320px;
      min-width: 320px;

      & > img {
        transform: scale(1.05);
      }
    }

    .blog-card__info {
      padding-left: 16px;
      padding-right: 32px;
    }
  }
}

.blog-right {
  position: sticky;
  top: 100px;
  height: 100%;

  h4 {
    margin-top: 16px;
    font-weight: normal;
    padding: 2px 16px;
    margin-bottom: 12px;
    border-left: 4px solid #E63657;
  }

  h4:first-child {
    margin-top: 0;
  }

  .zhuanlan-slideshow {
    height: 380px;
    overflow: hidden;

    & > img {
      object-fit: cover;
      border-radius: 8px;
    }
  }
}
 
</style>