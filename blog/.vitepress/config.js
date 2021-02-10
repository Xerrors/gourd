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
      author: "玉川",
      mail: "xerrors@163.com",
      github: "https://www.github.com/Xerrors",
      search: false,
      sidebar: false,
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