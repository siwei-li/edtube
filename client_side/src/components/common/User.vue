<template>
<div>
    <div v-if="!$auth.loading">
      <!-- show login when not authenticated -->
      <el-button v-if="!$auth.isAuthenticated" @click="login">Log in</el-button>
      <el-button type="primary" v-if="!$auth.isAuthenticated" @click="signup">Sign Up</el-button>
      <!-- show logout when authenticated -->
      <div v-if="$auth.isAuthenticated"> 
        Welcome, {{$auth.user.name}}!
        Info:{{loginMsg}}
        <button @click="logout">Log out</button>
      </div>
    </div>
<!--  <div @click="this.window.location='http://localhost:8000/login/auth0'">-->
  <div>
    <button @click="callApi">backend</button>
  </div>
</div>
</template>

<script>
import axios from "axios";
import { getInstance } from '@/auth/index.js';


export default {
  name: "User",
  data() {
    return {
      loginMsg: "",

    }
  },
  // created() {
  //   this.init(this.callApi());
  // },
  methods:{
    // init(fn) {
    //   // have to do this nonsense to make sure auth0Client is ready
    //   var instance = getInstance();
    //   instance.$watch("loading", loading => {
    //     if (loading === false) {
    //       fn(instance);
    //     }
    //   });
    // },

    async callApi(instance) {
      const token = await this.$auth.getTokenSilently();
      // await instance.getTokenSilently().then((authToken) => {
      //   console.log('token', authToken);
      // });
      console.log(token)

      // Use Axios to make a call to the API
      const { data } = await axios.get('/login/auth0', {
        headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        }
      });

      this.loginMsg = data;
      console.log("API called and fetched.");
    },
    login() {
      this.$auth.loginWithRedirect();
      // this.$options.methods.callApi();

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