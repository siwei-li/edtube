<template>
  <div class="layout">
    <el-container class="main-layout-home">
      <el-header class="el-header-home">
        <Header/>
      </el-header>

      <el-container>
        <el-aside width="200px" class="el-menu-layout-home">
          <Menu/>
        </el-aside>

        <el-container class="main-container-home">
          <el-main>
            <slot></slot>
          </el-main>

          <el-footer>
            <Footer></Footer>
          </el-footer>
        </el-container>

      </el-container>

    </el-container>

  </div>
</template>

<script>
import Header from '@/components/common/Header.vue'
import Menu from '@/components/common/Menu.vue'
import Footer from '@/components/common/Footer.vue'

export default {
  name: 'Layout',
  components: {
    Header,
    Menu,
    Footer
  },
}
</script>

<style>
.main-layout-home {
  position: relative;
}

.el-menu-layout-home {
  position: fixed;
  /*background: grey !important;*/
  left: 0;
  margin-top: 60px;
  z-index: 998;
}

.el-header-home {
  text-align: center;
  line-height: 60px;
  position: fixed;
  background-color: white;
  height: 12%;
  top: 0;
  left: 0;
  right: 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .3);
  z-index: 999;
}

.main-container-home {
  margin-top: 60px;
  /*margin-left: 90px;*/
  /*margin-right: 20px;*/
  margin-left: 60px;
  /*background-color: #5f9cf2;*/
}
</style>