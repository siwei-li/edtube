<template>
  <el-row type="flex" justify="flex-start" class="wrapper">
    <div v-if="!this.$auth.loading">
      <div v-if="!this.$auth.isAuthenticated">
        <el-avatar icon="el-icon-user-solid"></el-avatar>
      </div>
      <div v-if="this.$auth.isAuthenticated">
        <el-avatar :src="this.$auth.user.picture" slot="reference"></el-avatar>
      </div>
    </div>

    <div id="input">
      <el-input
          type="textarea"
          :autosize="{ minRows: 2 }"
          placeholder="Share your knowledge with the world!"
          v-model="textarea"
          @focus="authLogin"
      ></el-input>
      <el-button @click="onReply">Send</el-button>
    </div>
  </el-row>
</template>

<script>
export default {
  name: "Textarea",
  data() {
    return {
      textarea: "",
    }
  },
  methods: {
    authLogin() {
      if (!this.$auth.loading) {
        if (!this.$auth.isAuthenticated) {
          this.$auth.loginWithPopup();
        }
      }
    },
    onReply() {
      //TODO
      // let comment = new Comment(1, this.$auth.user.nickname, this.textarea);
      let comment = {
        id: "222",
        nickName: "me",
        good: 500,
        bad: 9,
        replyData: "好棒哇哇哇哇哇",
        showTextarea: false,
        replyList: [],
        timestamp: 1600670910515,
      };
      this.commentList.unshift(comment);
      this.textarea = "";
    }
  },
}
</script>

<style lang="less" scoped>
.wrapper {
  margin-left: 15px;

  #input {
    margin-left: 15px;
    width: 80vw;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }

  button {
    margin-top: 2px;
  }
}
</style>