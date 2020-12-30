<template>
<div>
    <div v-if="!$auth.loading">
      <!-- show login when not authenticated -->
      <el-button v-if="!$auth.isAuthenticated" @click="login">Log in</el-button>
      <el-button v-if="!$auth.isAuthenticated" @click="signup">Sign Up</el-button>
      <!-- show logout when authenticated -->
      <div v-if="$auth.isAuthenticated"> 
        Welcome, {{$auth.user.name}}!
        <button @click="logout">Log out</button>
      </div>
    </div>
</div>
</template>

<script>
export default {
  name: "User",
  methods:{
        // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    signup() {
      this.$auth.loginWithRedirect({screen_hint: 'signup' });
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