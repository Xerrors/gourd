<template>
  <div class="edit-container">
    <div class="edit-box">
      <v-md-editor 
        v-model="myEditor.text" 
        :disabled-menus="[]"
        right-toolbar="preview toc sync-scroll | upload"
        @upload-image="handleUploadImage"
        @save="handleSave"
        :toolbar="toolbar"
        ></v-md-editor>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from 'vue';
import request from "../utils/request";
import { parseTime } from '../utils/format';
import { message } from "ant-design-vue";

import { useRoute, useRouter } from "vue-router";

export default defineComponent({
  name: "NewPage",
  setup() {
    const date:string = parseTime(new Date());
    const oriText:string = '---\ntitle: \ndate: ' + date + '\npermalink: draft\ncover: \ntag: \n - blog\n - \ncategories: \n\n---\n';

    let route = useRoute();
    let router = useRouter();

    let myEditor = reactive({
      text: oriText,
      resetContent: () => {
        myEditor.text = oriText;
      }
    })

    let toolbar = reactive({
      upload: {
        icon: 'v-md-icon-tip',
        title: '上传',
        action(editor:any) {
          console.log(myEditor.text);
          new Promise((resolve, reject): void => {
              request({
                url: "/api/articles/md_source",
                method: "post",
                data: myEditor.text,
                headers: { 
                  'Content-Type': 'text/plain'
                },
                params: {
                  path: route.params.path,
                },
              })
                .then((res) => {
                  message.success(res.data.message);
                  resolve(res);
                })
                .catch((err) => {
                  reject(err);
                });
            });
        },
      },
      clear: {
        icon: 'v-md-icon-clear',
        title: '重置内容',
        action(editor:any) {
          myEditor.resetContent();
          localStorage.removeItem(String(route.params.path));
        }
      },
    })

    onMounted(() => {
      console.log(route.params.path);
      if (route.params.path == "draft") {
        if (localStorage.getItem("draft")) {
          myEditor.text = localStorage.getItem("draft");
        }
      } else {
        new Promise((resolve, reject): void => {
          request({
            url: "/api/articles/md_source",
            method: "get",
            params: {
              path: route.params.path
            }
          })
            .then((res) => {
              myEditor.text = res.data.data;
              resolve(res);
            })
            .catch((err) => {
              message.error("所访问的资源不存在")
              router.push('/edit/draft');
              reject(err);
            });
        });
      }
    })

    return {
      myEditor,
      toolbar,
    }
  },
  methods: {
    handleUploadImage(event:any, insertImage:any, files:any) {
      // 拿到 files 之后上传到文件服务器，然后向编辑框中插入对应的内容
      console.log(files);

      // // 此处只做示例
      // insertImage({
      //   url:
      //     'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1269952892,3525182336&fm=26&gp=0.jpg',
      //   desc: '七龙珠',
      //   // width: 'auto',
      //   // height: 'auto',
      // });
    },
    handleSave(text:string, html:string) {
      localStorage.draft=text;
    }
  },
})
</script>

<style lang="scss">
.edit-container {
  width: 100%;
  min-height: 100vh;
  background: #e6e6e6;
  // padding-top: 40px;

  .edit-box {
    // width: 1000px;
    min-height: 500px;

    margin: 0 auto;
    background: white;
    border: 1px solid #f2f2f2;

    .v-md-editor {
      height: calc(100vh - 2px);
    }
  }
}
</style>
