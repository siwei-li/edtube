<template>
  <div id="app">

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/profile">Profile</router-link> -->
    <router-view/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'


export default {
  name: 'app',
  components: {
    // HelloWorld,
    // Home
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}


body{
  margin:0;
  padding:0;
}

</style>
