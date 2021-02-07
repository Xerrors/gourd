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
      search: false,
      nav: [
        { text: "首页", link: "/" },
        { text: "Guide", link: "/pages/guide" },
        { text: "Blog", link: "/pages/blogs" },
      ],
    },
    dest: "public",
  };

  return config;
}
module.exports = getConfig();