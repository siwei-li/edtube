<template>
  <div>
    <div v-if="!this.$auth.loading">
      <el-button v-if="!this.$auth.isAuthenticated" @click="login">Log in</el-button>
      <el-button type="primary" v-if="!this.$auth.isAuthenticated" @click="signup">Sign Up</el-button>

      <div v-if="this.$auth.isAuthenticated">
        <!--        Welcome, {{$auth.user.name}}!-->
                <button @click="logout">Log out</button>
        <el-dropdown class="user-dropdown">
          <el-avatar :src="this.$auth.user.picture" class="user-avatar"></el-avatar>
          <el-dropdown-menu slot="dropdown" >
            <el-dropdown-item>查看</el-dropdown-item>
            <el-dropdown-item>新增</el-dropdown-item>
            <el-dropdown-item>删除</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>

      </div>
    </div>
  </div>
</template>

<script>
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
.user-dropdown {
  margin-top: 10px;
  height:40px;
}

</style>