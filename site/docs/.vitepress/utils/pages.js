const fs = require("mz/fs");
const globby = require("globby");
const matter = require("gray-matter");

const compareDate = (obj1, obj2) => {
  return obj1.frontMatter.date < obj2.frontMatter.date ? 1 : -1;
};

function parseTime(time, cFormat) {
  if (arguments.length === 0) {
      return null
  }
  const format = cFormat || '{y}-{m}-{d} {h}:{i}:{s}'
  let date = time;
  const formatObj = {
      y: date.getFullYear(),
      m: date.getMonth() + 1,
      d: date.getDate(),
      h: date.getHours(),
      i: date.getMinutes(),
      s: date.getSeconds(),
      a: date.getDay()
  }
  const time_str = format.replace(/{(y|m|d|h|i|s|a)+}/g, (result, key) => {
      let value = formatObj[key]
      // Note: getDay() returns 0 on Sunday
      if (key === 'a') { return ['日', '一', '二', '三', '四', '五', '六'][value] }
      if (result.length > 0 && value < 10) {
          value = '0' + value
      }
      return value || 0
  })
  return time_str
}

const getRandomCover = () => {
  return 'https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519142253.png';
}

module.exports = async () => {
  const paths = await globby(["**.md"], {
    ignore: ["node_modules"],
  });
  let pages = await Promise.all(
    paths.map(async (item) => {
      const content = await fs.readFile(item, "utf-8");
      const { data } = matter(content);

      if (!data.cover) {
        data.cover = getRandomCover();
      }

      data.formattedDate = parseTime(new Date(data.date), "{y}年{m}月{d}日")

      return {
        frontMatter: data,
        regularPath: `/${item.replace(".md", ".html")}`,
        relativePath: item,
      };
    })
  );
  pages = pages.filter((item) => !Boolean(item.frontMatter.customLayout)
                              && !item.frontMatter.home
                              && !item.frontMatter.page);
  
  pages.sort(compareDate);
  return pages;
};