const getPages = require("./utils/pages");

async function getConfig() {
  const config = {
    head: [
      ["meta", { name: "keywords", content: "Gourd" }],
      ['link', { rel: 'manifest', href: '/manifest.json' }],
      ['script', { src: '/font.js', type: 'application/javascript' }],
      ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }]
    ],
    title: "Gourd",
    lang: 'zh-CN',
    description: 'Just playing around.',
    extend: '@vitepress/theme-default',
    themeConfig: {
      pages: await getPages(),
      author: "Xerrors",
      mail: "xerrors@163.com",
      info: "江南大学 · 2017级 · 计算机科学与技术专业 · 学习方向：计算机视觉、图像处理",
      github: "https://www.github.com/Xerrors",
      search: false,
      sidebar: "auto",
      nav: [
        { text: "测试", link: "/pages/guide" },
        { text: "博客", link: "/pages/blogs" },
        { text: "动态", link: "/pages/zone" },
        { text: "关于", link: "/pages/about" },
        { text: "友链", link: "/pages/friends" },
      ],
    },
    markdown: {
      // lineNumbers: true,
      config: (md) => {
        md.use(require('@iktakahiro/markdown-it-katex'));
        md.render = function () {
          return md
            .render
            .apply(this, arguments)
            .replace(/<span class="katex">/g, '<span v-pre class="katex">')
        }
      },
    },
    dest: "public",
  };

  return config;
}
module.exports = getConfig();