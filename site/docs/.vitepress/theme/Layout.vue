<template>
  <h1>{{ $site.title }}</h1>
  <p>{{ $site.description }}</p>
  <Content/><!-- make sure to include markdown outlet -->
  <Comment/>
</template>

<script>
import Comment from "./components/comment.vue"

export default {
  name: "layout",
  components: {
    Comment,
  }
}
</script>