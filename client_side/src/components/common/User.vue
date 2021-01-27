<template>
  <div style="height: 60px">
    <div v-if="!this.$auth.loading">

      <div v-if="!this.$auth.isAuthenticated" class="button-group">
        <div class="hidden-xs-and-down" style="width: 190px">
          <el-button @click="login">Log in</el-button>
          <el-button type="primary" @click="signup">Sign Up</el-button>
        </div>
      </div>

      <div v-if="this.$auth.isAuthenticated" class="user-popover">
        <!--        Welcome, {{$auth.user.name}}!-->
        <!--                <button @click="logout">Log out</button>-->
        <!--        <el-dropdown class="user-dropdown">-->
        <!--          <el-avatar :src="this.$auth.user.picture" class="user-avatar"></el-avatar>-->
        <!--          <el-dropdown-menu slot="dropdown" >-->
        <!--            <el-dropdown-item>查看</el-dropdown-item>-->
        <!--            <el-dropdown-item>新增</el-dropdown-item>-->
        <!--            <el-dropdown-item>删除</el-dropdown-item>-->
        <!--          </el-dropdown-menu>-->
        <!--        </el-dropdown>-->

        <el-popover
            placement="bottom-end"
            title="标题"
            width="200"
            trigger="hover"
            content="这是一段内容,这是一段内容,这是一段内容,这是一段内容。">
          <el-avatar :src="this.$auth.user.picture" class="user-avatar" slot="reference"></el-avatar>
        </el-popover>
      </div>

    </div>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css';

export default {
  name: "User",
  created: function () {

  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    signup() {
      this.$auth.loginWithRedirect({screen_hint: 'signup'});
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    }
  }
}
</script>

<style>
.button-group {
  height: 60px;
  margin: 0 auto;
}

/*.user-dropdown {*/
/*  margin-top: 10px;*/
/*  height: 40px;*/
/*}*/

.user-popover {
  width: 40px;
  height: 40px;
  margin-top: 10px;
}

</style>