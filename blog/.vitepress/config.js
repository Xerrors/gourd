const getPages = require("./utils/pages");

async function getConfig() {
  const config = {
    head: [
      ["meta", { name: "keywords", content: "Gourd" }],
      ['link', { rel: 'manifest', href: '/manifest.json' }],
      ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }]
    ],
    extend: '@vitepress/theme-default',
    title: "Gourd",
    lang: 'zh-CN',
    description: 'Just playing around.',
    themeConfig: {
      pages: await getPages(),
      author: "Xerrors",
      mail: "xerrors@163.com",
      info: "江南大学 · 2017级 · 计算机科学与技术专业 · 学习方向：计算机视觉、图像处理",
      github: "https://www.github.com/Xerrors",
      search: false,
      sidebar: "auto",
      nav: [
        { text: "首页", link: "/" },
        { text: "测试", link: "/pages/guide" },
        { text: "博客", link: "/pages/blogs" },
        { text: "动态", link: "/pages/zone" },
        { text: "关于", link: "/pages/about" },
      ],
    },
    dest: "public",
  };

  return config;
}
module.exports = getConfig();