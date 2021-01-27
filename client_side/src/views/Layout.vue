<template>
  <div class="layout">
    <div class="header-home">
      <Header/>
    </div>
    <Drawer></Drawer>

    <div class="main-container-home">
      <slot></slot>
    </div>

    <!--          <div>-->
    <!--            <Footer></Footer>-->
    <!--          </div>-->

  </div>
</template>

<script>
import Header from '@/components/common/Header.vue'
import Footer from '@/components/common/Footer.vue'
import Drawer from "@/components/common/Drawer";

export default {
  name: 'Layout',
  components: {
    Header,
    Footer,
    Drawer,
  },
}
</script>

<style>
.layout {
  position: relative;
}

/*.el-menu-layout-home {*/
/*  position: fixed;*/
/*  !*background: grey !important;*!*/
/*  left: 0;*/
/*  margin-top: 60px;*/
/*  z-index: 998;*/
/*}*/


.main-container-home {
  margin-top: 60px;
  padding: 10px;
  z-index: 998;
  /*margin-right: 20px;*/
  /*margin-left: 20px;*/
}
</style>