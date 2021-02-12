<template>
  <div class="blog-container">
    <div class="slideshow">
      <Shuffler :sliderArray="frontmatter.banner"/>
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
      <!-- <a-input-search
        v-model:value="searcher.value"
        placeholder="input search text"
        style="width: 200px"
        @search="searcher.onSearch"
      /> -->
    </div>

    <div class="blogs">
      <div
        v-for="(page, ind) in filtedPages"
        :key="ind"
        >
        <div class="week-card" v-if="page.frontMatter.categories=='周报'">
          <div class="week-card__header">
            {{ page.frontMatter.formattedDate }}周报
          </div>
          <div class="week-card__title" @click="goToPage(page.regularPath)">
            {{ page.frontMatter.title }}
          </div>
          <div class="week-card__cover" @click="goToPage(page.regularPath)">
            <img :src="page.frontMatter.cover" alt="">
          </div>
          <div class="week-card__content">
            {{ page.frontMatter.abstract }}
          </div>
        </div>
        <div class="blog-card" v-else>
          <div class="blog-card__image" @click="goToPage(page.regularPath)">
            <img :src="page.frontMatter.cover + '?x-oss-process=image/resize,m_fill,h_180,w_340'" alt="">
          </div>

          <div class="blog-card__info">
            <h3 @click="goToPage(page.regularPath)">{{ page.frontMatter.title }}</h3>
            <span>{{ page.frontMatter.formattedDate }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="blog-right">
      <div class="adversizement">
        广告位招租
      </div>

      <h4>我的专栏</h4>

      <div class="zhuanlan-slideshow">
        <img src="https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20201009130905.png" alt="">
      </div>

    </div>
  </div>
</template>

<script>
import { defineComponent, ref, reactive, computed } from 'vue';
import { useSiteDataByRoute, useRouter, useFrontmatter } from "vitepress";
import { formatTime } from "../../utils/format";
import { SearchOutlined } from '@ant-design/icons-vue';

import Shuffler from "./Shuffler.vue";

export default defineComponent({
  name: "Blog",
  components: {
    SearchOutlined,
    Shuffler,
  },
  setup() {
    const siteData = useSiteDataByRoute().value;
    const frontmatter = useFrontmatter().value;

    const searcher = reactive({
      value: "",
      onSearch: () => {
        console.log("onSearch");
      }
    });

    const labels = frontmatter.blogCategories;
    const categories = reactive({
      labels: labels,
      active: labels[0] || "全部",
      selectCategory: (link) => {
        categories.active = link;
      }
    })

    let pages = siteData.themeConfig.pages;
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
      frontmatter,
      categories,
      goToPage,
      searcher,
    }
  }
})


</script>

<style lang="scss" scoped>
.blog-container {
  margin: 0 auto;
  margin-top: var(--header-height);
  width: var(--page-width-w);

  display: grid;
  grid-template-columns: 9fr 3fr;
  grid-template-rows: 380px 60px auto;
  grid-column-gap: 30px;
  grid-row-gap: 20px;
}

.slideshow {
  width: 100%;
  height: 100%;
  border-radius: 4px;
  overflow: hidden;

  grid-column-start: span 2;

  // img {
  //   object-fit: cover;
  //   width: 100%;
  // }
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
    color: var(--accent-color);
    padding: 12px 20px;

    border-bottom: 4px solid var(--accent-color);
  }
}

.blogs {
  .blog-card {
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

.blogs .week-card {
  display: grid;
  grid-template-rows: 50px 30px 100px;
  grid-template-columns: auto 256px;
  grid-gap: 14px;

  padding: 24px 28px;
  border: 1px solid #f2f2f2;
  margin-bottom: 24px;

  &__header {
    grid-column: span 2;

    font-weight: bold;
    font-size: 24px;
    line-height: 24px;
    color: var(--accent-color);

    border-bottom: 2px solid #f2f2f2;
    margin-bottom: 10px;
  }

  &__title {
    font-weight: bold;
    font-size: 24px;
    line-height: 24px;
    cursor: pointer;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }

  &__content {
    font-size: 16px;
    line-height: 24px;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  &__cover {
    grid-row: span 2;
    width: 100%;
    overflow: hidden;
    cursor: pointer;

    img {
      object-fit: cover;
      height: 100%;
      border-radius: 4px;
    }
  }

}

.blog-right {
  position: sticky;
  top: var(--header-height);
  height: fit-content;

  .adversizement {
    background: white;
    min-height: 100px;
    border: 1px solid #f2f2f2;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
  }

  h4 {
    margin-top: 16px;
    font-weight: normal;
    padding: 2px 16px;
    margin-bottom: 12px;
    border-left: 4px solid var(--accent-color);
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

/* ----------------------------------------------
 * Generated by Animista on 2021-2-10 19:0:30
 * Licensed under FreeBSD License.
 * See http://animista.net/license for more info. 
 * w: http://animista.net, t: @cssanimista
 * ---------------------------------------------- */

/**
 * ----------------------------------------
 * animation slide-in-blurred-bottom
 * ----------------------------------------
 */
@keyframes slide-in-blurred-bottom {
  0% {
    transform: translateY(400px) scaleX(0.8);
    transform-origin: 50% 100%;
    opacity: 0;
  }
  100% {
    transform: translateY(0) scaleX(1);
    transform-origin: 50% 50%;
    opacity: 1;
  }
}

</style>