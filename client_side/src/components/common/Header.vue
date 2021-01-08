<template>
  <div class="header">
    <el-row type="flex" class="row-bg" justify="space-between">

      <div class="togl">
        <el-button @click="toglMenu" icon="el-icon-more" circle></el-button>
      </div>

      <div class="Search">
        Search
      </div>


      <div class="user">
        <User/>
      </div>

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
.togl {
  margin-left: -8px;
}
</style>