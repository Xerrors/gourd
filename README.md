# Gourd 🎅

> 【提醒】项目处于起步阶段 In Progress

## 项目介绍

项目的功能分为三个部分，博客网页、后台管理系统、后端数据支持；

### 简单介绍

首先**博客网站**所实现的就是一个博客的基本功能，同时在 Markkdown 写作上做了部分阅读增强，如交互程序、标注、codesnip 以及更多样式自定义部分。技术实现方面采用 Vue3 + vitepress + typescript 框架来搭建前端网站，等待明年年初 vitepress 发布 1.0 正式版之后就着手开发，实现完全自定义的前端博客。 

其次**后台管理系统**是整个网站的“中控室”，相当于部分博客系统的管理员账户。后端部分的实现使用 vue3 + vite + typescript 的技术，同时由于工程项目更多，所以也会使用到 vue-router 的路由管理机制，以及 Vuex 的数据状态管理机制。

**服务器后端部分**采用 Python 的 Flask 框架开发出简单易用的后端程序，因为整个项目在后端部分的任务不是很重，只是一些简单的数据处理工作，所以在实现的时候没有必要使用很负责的 Java 类后端，同时由于前后端的可分离性，本项目也采用 MVVM 模型，后端仅仅只是处理数据和执行脚本，在与前端部分的交互上面，使用 Restful Apis 进行数据传输；

### 项目功能

这是一个个人创作者的个人网站，也是理科生的一种浪漫，折腾自己的网站，在网站上集成自己想要的功能。除了最基本的前端博客功能，具体功能设计参考思维导图：[GitMind.cn](https://gitmind.cn/app/doc/e43752359)

### 项目相关资源

- 博客设计文档 by [Notion.so](https://www.notion.so/krance/1cbf60650c0f455cbb13c9fbbb96f0cb)
- 后台设计文档 by [Notion.so](https://www.notion.so/krance/Dashboard-0940dcf050b84838b16e6b47b6b69cf6)
- 后端设计文档 by [Notion.so](https://www.notion.so/krance/eada9f4c33d94e70b027bd9e5dd31ff3)
- 博客设计的思维导图-[GitMind.cn](https://gitmind.cn/app/doc/e43752359)
- 开发日志-[CHANGELOG](./docs/CHANGELOG.md)
- 基于 [vitepress](https://github.com/vuejs/vitepress)
- BootStrap [v5](https://v5.bootcss.com)

