<template>
<div class="home">

  <div class="header-home">
    <Header/>
  </div>
  <Drawer></Drawer>

  <div class="menu-home">
    <Menu></Menu>
  </div>

  <div class="main-home">
    <div class="list-wrapper">
      <VideoList listTitle="Featured"></VideoList>
    </div>
  </div>


</div>
</template>

<script>
// import Layout from '@/views/Layout.vue'
import Menu from '@/components/common/Menu.vue'
import Header from "@/components/common/Header.vue"
import VideoList from '@/components/video/VideoList.vue'
import Drawer from "@/components/common/Drawer.vue";

export default {
  name: 'Home',
  components: {
    // Layout,
    Header,
    VideoList,
    Menu,
    Drawer,
  },
  data() {
    return {}
  }
}
</script>

<style>

.menu-home {
  /*width: 60px;*/
  position: fixed;
  left: 0;
  top: 0;
  margin-top: 60px;
  z-index: 998;
}

.main-home {
  margin-top: 80px;
  padding: 0 20px 0 20px;
  margin-left: 60px;
}

.list-wrapper {
  padding-left: 5px;
}
</style>
