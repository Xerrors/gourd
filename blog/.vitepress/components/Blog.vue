<template>
  <div class="blog-container">
    <div class="slideshow">
      <img src="https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519142253.png" alt="轮播图">
    </div>

    <div class="blog-left">
      <ul>
        <li
          v-for="(cat, ind) in categorylinks"
          :key="ind"
          :class="{active: activelink == cat}"
          >
          {{ cat }}
        </li>
      </ul>

      <div class="blogs">
        <div
          class="blog-card"
          v-for="(page, ind) in pages"
          :key="ind"
          >
          <div class="blog-card__image">
            <img src="https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519142253.png" alt="">
          </div>

          <div class="blog-card__info">
            <h3>{{ page.frontmatter.title }}</h3>
            <span>{{ page.frontmatter.date }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="blog-right">
      <div class="search-box">
        搜索
      </div>

      <h3>我的专栏</h3>

      <div class="zhuanlan-slideshow">
        <img src="https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20201009130905.png" alt="">
      </div>

      <h3>标签查询</h3>

      
    </div>
  </div>
</template>

<script setup>
const categorylinks = ["全部", "前端", "人工智能", "算法", "基础"];
const activelink = "全部";

</script>