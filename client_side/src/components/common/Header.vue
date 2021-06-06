<template>
  <div class="header">
    <el-row type="flex" class="row-bg" style="height: 60px" justify="space-between">

      <el-row type="flex">
        <div class="togl">
          <el-button @click="toglMenu" icon="el-icon-more" circle></el-button>
        </div>

        <div class="header-logo">
          <img style="height: 50px;margin-right: 10px;margin-top: 5px" src="@/assets/apple-touch-icon.png">
          <h2 style="margin-top: 3px">EdTube</h2>
        </div>
      </el-row>

      <!--      <el-row type="flex" justify="space-between">-->
      <!--        <el-col>-->


      <div class="search">
        <Search></Search>
      </div>

      <div class="user">
        <User/>
      </div>

      <!--      </el-col>-->
      <!--      </el-row>-->

    </el-row>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css';
import User from '@/components/common/User.vue'
import Search from '@/components/common/Search.vue'

export default {
  name: "Header",
  components: {
    User,
    Search
  },
  methods: {
    toglMenu() {
      return this.$store.commit("toggleMenu");
    }
  },
}
</script>

<style>
.header {
  text-align: center;
  line-height: 60px;
  position: fixed;
  background-color: white;
  /*height: 12%;*/
  top: 0;
  left: 0;
  right: 0;
  padding: 0 20px 0 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .3);
  z-index: 999;
}

.header-logo {
  width: 200px;
  margin-left: 15px;
  justify-content: flex-start;
  display: flex;
  flex-wrap: nowrap;
}

.togl {
  margin-left: -5px;
}

.search {
  margin-left: 10px;
}

.user {
  margin-left: 10px;
}
</style>