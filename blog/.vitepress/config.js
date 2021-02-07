const getPages = require("./utils/pages");

async function getConfig() {
  const config = {
    head: [
      ["meta", { name: "keywords", content: "Gourd" }],
      ["link", { rel: "icon", href: "/favicon.ico" }],
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
        { text: "Guide", link: "/guide" },
        { text: "Blog", link: "/blogs" },
      ],
    },
    dest: "public",
  };

  return config;
}
module.exports = getConfig();