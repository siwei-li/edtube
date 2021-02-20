<template>
  <el-row type="flex" justify="flex-start" class="wrapper">
    <div>
      <el-avatar icon="el-icon-user-solid"></el-avatar>
    </div>

    <div class="text-wrapper">
      <span>{{ comment.nickName }}</span>
      <span style="margin-left: 15px">{{ comment.timestamp }}</span>
      <p>{{ comment.replyData }}</p>

      <div>
      <span class="rt">
        <i class="icon-good"></i>
        <span>{{ comment.good > 0 ? comment.good : '' }}</span>
        <i class="icon-bad"></i>
        <span>{{ comment.bad > 0 ? comment.bad : '' }}</span>
      </span>
        <span class="handle-reply" @click="comment.showTextarea=!comment.showTextarea">
        Make A Reply
        <i v-show="!comment.showTextarea" class="el-icon-arrow-down"></i>
        <i v-show="comment.showTextarea" class="el-icon-arrow-up"></i>
      </span>
        <transition name="el-fade-in">
          <div v-show="comment.showTextarea" class="transition-box">
            <Textarea></Textarea>
          </div>
        </transition>
      </div>
    </div>

  </el-row>
</template>

<script>
import Textarea from "@/components/comment/Textarea";

export default {
  name: "post",
  components: {Textarea},
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
}
</script>

<style scoped>

</style>