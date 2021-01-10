## 需求分析

### 1. 信息的存储与管理

先整理以一下整个网站可能会用到的数据：

- 动态、日报信息
- 文章的点赞量（后台可见）
- 文章的访问量（后台可见，一分钟内，同一IP算一次访问）
- 文章的评论（不一定会实现）

使用 Python 解析项目文件夹下面的 markdown 文件；由于所有文章都是以文件夹的结构存放于项目中的，如果将文章信息保存在数据库里面，之后的迁移工作将会变得很麻烦，所以想要获取所有文章信息，可以使用 Python 解析所有 markdown 文件的 frontmatter 这样就可以将所有的信息实时更新出来。

访问量就是进一次页面请求一次pv接口；点赞的话因为没有注册登录，现在的做法是当点赞时将用户ip传给后端，如果ip在数据库表里，那么点赞无效；否则把ip存到数据库，前端显示ipList的length。

### 2. 密码等安全措施的验证

对于一些需要加密的页面，就需要自己的后端服务了，需要进行验证、加密等等操作。所以整体而言，对于数据的存储可以是用 leancloud，但是对于验证之类的服务，还是需要使用后端来实现；也就是跟现在的处理逻辑差不多。

### 3. 服务器状态检测或者服务器执行指令

待定


### 4. 数据的存储形式

关于数据是存储在类似于 json 的文件中？还是存储在数据库中？

1. 对于静态的数据，不需要进行反复的增删改查的，使用「JSON」保存；
2. 对于线性文件，结构不复杂的，使用「JSON」保存；
3. 对于需要查询筛选、经常访问的数据，使用「数据库」存储；

## 开发日志

### 1. 创建虚拟环境以及生成依赖

```sh
conda create -n flask python=3.7
conda activate flask

pip install falsk
pip install pipreqs

# 使用以下命令可以将当前项目的所有依赖生成到 requirements.txt 里面
pipreqs .

# 安装
pip install -r requirements.txt
```

看到一个很好的教程：https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
API：http://www.pythondoc.com/flask-restful/
