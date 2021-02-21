---
title: 给 Vuepress 添加暗色夜间模式
permalink: vuepress-dark-mode
date: 2020-05-19 02:37:45
cover: https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519142253.png
tags: 
 - Vuepress
 - 前端
categories: 前端
---

<div class="header">
  <img class="header__cover" :src="$frontmatter.cover" alt="cover" />
  <h1 class="header__title">{{ $frontmatter.title }}</h1>
  <p class="header__info">{{ $frontmatter.date }}</p>
</div>

<script>
// import { formatTime } from "";
</script>

<style lang="scss" scoped>
.header {
  &__cover {
    border-radius: 4px;
  }

  &__title {
    font-size: 2rem;
  }

  &__info {
    font-size: 14px;
    line-height: 24px;
    color: #41414E;
  }
}
</style>

## 1. 前言

随着各个系统都加入了「亮色/暗色模式」切换，Chrome 和 Edge 浏览器也支持了根据系统切换主题，作为互联网前沿的弄潮儿（没错，说你呢），咱们也要追上潮流不是，所以通过这篇文章你可以学习到如何在自己的 Vuepress 博客里面使用暗色模式。[预览](https://www.xerrors.fun)

<!--more-->

前提：如果想要完成这个工作，需要一定的知识储备：

- 有过使用 Vue 开发的经验
- 了解 Stylus 的用法（几分钟）
- 对 Vuepress 的自定义配置有一点点的了解，可以参考「[Vuepress 改造指南](https://www.xerrors.fun/decorate-vuepress/)」

当然如果是单纯想要做一个好看的博客网站，同时还想要支持暗色模式的话，建议直接使用「 [vuepress-theme-reco](https://vuepress-theme-reco.recoluan.com/) 」这个主题，配置起来方便省心，文档写的也很好。要是想要属于自己的主题、想要折腾锻炼自己的话，那么这篇文章绝对就是适合你的。

**高能提醒**：由于本人说话比较啰（dou）嗦（bi），所以下面会介绍的比较详细，能力强的同学可以使用旁边的目录索引跳转查看，我也尽量在重要的地方做出提醒；这次的暗色模式是我从早上八点折腾到晚上两点才弄完的，所以有必要来记录一下今天的工作。

做出一个出色的暗色模式需要几步？

1. **设计**出亮色以及暗色的配色；
2. 单独**测试**亮色以及暗色的表现；
3. 加上自动和手动**切换**主题的功能；

## 2. 设计主题配色

我虽然不是一个设计师，但是对美感有一定的追求，所以在配色的时候不能瞎配，要有准则！不然配出来的色很丑很杀马特，所以我先学习了很久的暗色模式。

我前一天晚上临睡前拜读了「[暗黑模式的8个设计要点](https://zhuanlan.zhihu.com/p/78713832)」，了解配色里面需要注意的坑，然后又通读「[深色模式的文本配色](https://www.zcool.com.cn/article/ZMTAxMjAxNg==.html)」，知道怎样去使用颜色的明暗关系来改变主题，还翻了翻「[UX/UI 設計師的 iOS 13 攻略](https://medium.com/uxabc/ios-13-8227dc9bcbb8)」。

我辗转反侧夜不能寐，最终我终于决定了「抄[少数派](https://sspai.com/)的配色」~毕竟人家是做好的嘛，我是个门外汉，正好少数派也是阅读类的网站（本身也是我很喜欢的一个网站）。

![少数派亮色主页](https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519020958.png)

所以我首先分析了少数派的亮色与暗色的文字以及背景的颜色（一个个取色器取出来的），下面是少数派官网的几个截图，上面对主要的颜色进行了标注（看不太清，没关系，后面有色卡）：

最终，提取出来有代表性的颜色，其他的几个相近的颜色可以在 stylus 里面由 lighten 和 darken 内置函数来转换得到：

```stylus
// dark mode scheme
$darkMainColor = #f94135 	 // 主题色
$darkPrimaryText = #ffffff   // 文字的首要颜色
$darkRegularText = #b8b8b8   // 常规文字颜色
$darkSecondaryText = #7f7f7f // 次要文字颜色
$darkBorder = #373737        // 边框颜色
$darkBoundary = #171514      // 边界颜色
$darkBgColor = #171514       // 深色背景颜色
$darkCard = #232222          // 深色卡片颜色
// light mode scheme
$lightMainColor = #d71a1b
$lightPrimaryText = #292525
$lightSecondaryText = #8e8787
$lightRegularText = #4c4e4d
$lightBorder = #e5e5e5
$lightBoundary = #e5e5e5
$lightBgColor = #f4f4f4
$lightCard = #ffffff
// 后期补充的遮罩颜色
$lightMask = rgba(255, 255, 255, 0.9) // 遮罩颜色
$darkMask = rgba(0, 0, 0, 0.9)
```

> stylus 里面的变量是没有必要使用 $ 开头的，但是因为使用习惯我加上了。

在上面为了有更好的适用性，我增加了两种模式的「遮罩颜色」，当然在此基础上还可以进行补充，比如设置不同等级的 border color，或者增加不同的 box-shadow 来实现更好的阴影以及高光效果，各位有才的同学自行添加。下面是两种主题的配色板：

这里顺带提一句题外话，少数派的配色使用的是「纯白背景 + 灰色字体 」和 「灰色背景 + 淡白字体」的组合，这样不会让眼睛因为对比度过大，而感受到刺激强让眼睛疲劳，同时主题的红色也在暗色模式下降低了亮度。

## 3. 测试亮色以及暗色的表现

由于我之前个人的编程习惯并不是很好，导致我写页面的时候，想用什么颜色就使用什么颜色 了，这也就导致现在要进行「全局管理」的话，非常的麻烦；

### 全局颜色管理

所以我花费了大量的时间在将全局的颜色进行统一。我们可以先将上面的颜色保存到 `.vuepress/style/palette.styl` 里面（方便测试），这样我们可以直接在主题中的其他文件中使用这些颜色变量不需要导入。

那么下一步就是修改自己的其他页面所用到的颜色了，我是用的是最笨的方法，「搜索替换」（我找不到更好的办法了）

这里我们需要把之前混乱的颜色，使用咱们上面「配色板」里面的颜色来替代，如果感觉颜色不够用，可以适当添加合适的颜色。

在进行两种模式的样式单独测试的时候，我们总不能老是搜索替换吧，最简单的使用办法就是变量代换，打个比方，我们有：

```stylus
// .vuepress/style/palette.styl
$darkMainColor = #f94135
$lightMainColor = #d71a1b
// 测试亮色主题时
$mainColor = $lightMainColor
// 测试暗色主题时
$mainColor = $darkMainColor
```

这样我们在其他文档中就可以使用 `$mainColor` 来表示主题色，也是为了咱们之后进行主题切换进行铺路；如：

```vue
<style lang="stylus" scoped>
.tetle
    color $mainColor
</style>
```

这里有几点是需要注意的：

1. 当涉及到颜色修改的时候，为了获得更好的效果，建议在浏览器的「调试窗口」修改来看看效果；
2. 两种模式需要「单独替换」，当亮色模式测试没有问题之后，再对暗色模式进行测试，当两个模式都单独测试完美之后，再进行主题切换工作。避免一次修改太多，出现问题不知道哪里出的问题。
3. 除了「 color 」之外，「 border 」的颜色也是要注意的地方。
4. 要么使用版本控制，要么对项目的副本进行操作，避免出现不可逆的问题出现。

### Element UI 的自定义主题

[在Vuepress中使用第三方库](https://wangtunan.github.io/blog/vuepress/#%E4%BD%BF%E7%94%A8%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93)

对于使用 Element UI 组件库的同学而言，修改上面的颜色还算可以接受，虽然繁琐了一点点，但是想要获得最终的结果也还是不难的；但是因为 ELement UI 组件库有自己的配色，想要修改内部的配色就会变得非常麻烦，比如我要把 tab 标签的边框颜色改成深色：

![](https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519030944.png)

我就需要下面这样才能达到效果：

```stylus
// 并没有完全遵循 stylus 的推荐语法，写的很乱，大家不要跟我学
<style lang="stylus">
.el-tabs--card>.el-tabs__header .el-tabs__item.is-active {
  border-bottom: none;
  color: $mainColor;
  font-weight: 600;
}

.el-tabs--card>.el-tabs__header {
  border-bottom: 1px solid $bgColor;
  .el-tabs__item {
    border-left-color: $bgColor
    color: $seconaryColor;
    &:hover {
      color: $mainColor;
    }
  }
}

.el-tabs--card>.el-tabs__header .el-tabs__nav {
  border: 1px solid $bgColor;
  border-bottom: none;
}
</style>
```

可以看到做一个小小的修改都非常非常的麻烦，要是涉及到修改弹窗之类复杂的组件的样式的话可能就要累死人了，那么以后每添加一个 Element UI 组件都要进行暗色模式适配，不可取；

所以我们可以使用 Element UI 的「[在线主题编辑器](https://element.eleme.cn/#/zh-CN/component/custom-theme) 」来生成我们所需要的暗色模式的主题文件，在这里可以可视化地修改各个颜色变量的值；这里的配色可以参考上面的配色卡，向下拉可以看到每个组件的表现效果；当我们把颜色调成我们想要的主题之后，点击右上角可以「下载」主题配置文件。

![Elementui](https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519082245.png)

下载之后会得到一个 style 压缩包，压缩包的目录结构如下：

```
style
 ├── config.json
 └── theme
     ├── fonts
     │   ├── element-icons.ttf
     │   └── element-icons.woff
     └── index.css // 我们想要的
```

由于有两份主题需要配置，所以最终会在 ElementUI 的主题编辑器里面得到两份样式文件，我们可以把两份 css 样式文件放在同一个样式文件夹里面，然后放入到项目文件夹里面，我选择放在了 `.vuepress/public/style/` 里面。config.json 文件我们暂时用不到。

```
 theme
 ├── fonts
 │   ├── element-icons.ttf
 │   └── element-icons.woff
 └── light.css // 我们想要的
 └── dark.css // 我们想要的
```

之后需要在 `.vuepress/enhanceApp.js` 引入样式文件，由于我们现在还没有加入主题切换功能，所以在测试的暗色模式的时候，就「仅仅」引入暗色的样式文件，测试亮色模式的时候「仅仅」引入亮色的样式文件。

```js
import Vue from 'vue'
import Element from 'element-ui'
import './public/style/theme/light.css' // 仅在测试亮色模式时启用
import './public/style/theme/dark.css'  // 仅在测试暗色模式时启用
import animated from 'animate.css'

export default ({
  Vue,
}) => {
  Vue.use(Element, animated)
}
```

这样我们就可以愉快的进行暗色模式的测试工作了，测试其实就是看看有没有颜色不对的地方，影响观感的地方，主要表现在以下几个地方：

- 对比度太强，也就是太刺眼，主要表现在边框以及字体上面；
- 对比度太低，字体或者组件处于难以看清的情况；
- 表面上看起来正常，但是存在 `:hover` `:focus` 等激活之后样式发生变化；

这是我的测试结果，尚可：


经过上面的修改之后，幸运的话，应该就可以是实现基本的亮色暗色主题的切换了。如果不是那么幸运的话，要多多在 devtools 里面调试，然后找到问题的源头，加油。


当当当当，大功告成！撒花~撒花~撒花~

这样做法是恰好适用于咱们的亮暗色模式切换，因为只有两个主题样式文件，要是样式很多的话，会导致样式文件很大，还是采用其他方法吧，看着配置好麻烦。

![动图演示](https://xerrors.oss-cn-shanghai.aliyuncs.com/imgs/20200519120409.gif)

我的博客的项目文件可以参考 [https://www.github.com/xerrors/Site](https://www.github.com/xerrors/Site)

## 总结以及参考资料

这篇文章是我从创建博客网站以来写的时间最长的一篇文章，写了大概 6 个多小时，尽可能把每个过程写得容易理解，很难解释的地方画图来理解；写作的内容应该还有不少需要改进的地方，也希望读者能够给我提出一些建议。

自从创建这个博客以来，每篇文章的访问量一般也就是个位数，最多的一篇是100+访问，相同的文章放在 CSDN 上面就会有更好的曝光度，访问量也更多；唉，写作之路很长，慢慢来，自己还只是这个领域的一个初学者，连入门者都算不上。

如果觉得这篇文章对你的开发有所帮助的话，可以在[博文](https://www.xerrors.fun/vuepress-dark-mode/)下方留言，写作者最需要的就是鼓励一直支持。

[1] [vuepress-theme-reco](https://vuepress-theme-reco.recoluan.com/)

[2] [暗黑模式的8个设计要点 - 知乎](https://zhuanlan.zhihu.com/p/78713832)

[3] [实践：拆解深色模式 文本配色 - 站酷 (ZCOOL)](https://www.zcool.com.cn/article/ZMTAxMjAxNg==.html)

[4] [UX/UI 設計師的 iOS 13 攻略 - Medium](https://medium.com/uxabc/ios-13-8227dc9bcbb8)

[5] [少数派 - 高效工作，品质生活](https://sspai.com/)

[6] [vuepress-theme-default-prefers-color-scheme | 雨无声](https://ououe.com/lib/vuepress-theme-default-prefers-color-scheme.html)

[7] [在线主题编辑器 - Element](https://element.eleme.cn/#/zh-CN/theme)

[8] [prefers-color-scheme - CSS（层叠样式表） | MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@media/prefers-color-scheme)

[9] [vue-基于elementui换肤[自定义主题] - CSDN博客](https://blog.csdn.net/young_Emily/article/details/78591261)

[10] [gulp.js - 基于流(stream)的自动化构建工具 | gulp.js 中文网](https://www.gulpjs.com.cn/)

<Comment />