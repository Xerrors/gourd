import os
import frontmatter

from config import BLOG_PATH

# def parse_md(arg, dirname, files):
#     for file in files:
#         markdown_path = os.path.join(dirname, file)
#         with open(markdown_path, encoding='UTF-8') as f:
#             md = frontmatter.load(f)
#             article_list.append(md.metadata['title'])


def get_article_list():
    assert os.path.exists(BLOG_PATH)
    article_list = []

    def extend_dir(path):
        for file in os.listdir(path):
            # 遍历所有文件
            markdown_path = os.path.join(path, file)

            # 如果是文件夹递归读取，否则读取文件
            if os.path.isdir(markdown_path):
                extend_dir(path=os.path.join(path, file))
            else:
                with open(markdown_path, encoding='UTF-8') as f:
                    md = frontmatter.load(f)
                    article_list.append(md.metadata)

    extend_dir(BLOG_PATH)
    return article_list