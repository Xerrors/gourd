<template>
  <div class="edit-container">
    <div class="edit-box">
      <v-md-editor 
        v-model="myEditor.text" 
        :disabled-menus="[]"
        right-toolbar="preview toc sync-scroll fullscreen | upload"
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


export default defineComponent({
  name: "NewPage",
  setup() {
    const date:string = parseTime(new Date());
    const oriText:string = '---\ntitle: \ndate: ' + date + '\npermalink: /temp-link\ncover: \ntag: \n - blog\n - \ncategories: \n\n---\n';

    let myEditor = reactive({
      text: oriText,
      resetContent: () => {
        console.log("heer2");
        myEditor.text = '---\ntitle: \ndate: ' + date + '\npermalink: /temp-link\ncover: \ntag: \n - blog\n - \ncategories: \n\n---\n';
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
                url: "/api/server/md_source",
                method: "post",
                data: myEditor.text,
                headers: { 
                  'Content-Type': 'text/plain'
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
          localStorage.removeItem("draft");
        }
      },
    })

    onMounted(() => {
      if (localStorage.draft) {
        myEditor.text = localStorage.getItem("draft");
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
