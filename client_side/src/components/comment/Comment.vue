<template>
  <div id="comment">
    <h3 style="margin-left: 5px">Comment</h3>
    <Textarea></Textarea>

    <div>
      <ul class="comment-list">
        <li v-for="comment in commentList">
          <Post :comment="comment"></Post>

          <ul class="reply-list" v-show="comment.replyList.length>0">
            <li v-for="reply in comment.replyList">
              <Post :comment="reply"></Post>
            </li>
          </ul>

        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import Textarea from "@/components/comment/Textarea";
import Post from "@/components/comment/Post";

export default {
  name: "Comment",
  components: {Textarea, Post,},
  data() {
    return {}
  },
  props: {
    commentList: {
      type: Array,
      required: true
    }
  },

}
</script>

<style lang="less" scoped>
.comment {
  //margin-left: 20px;
}

.comment-list {
  //margin-top: 20px;
  li {
    padding: 15px 0;
    display: block;

  }
}

.icon-good {
  margin-left: 10px;
}

.icon-bad {
  margin-left: 10px;
}

</style>