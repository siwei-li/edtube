<template>
<div>
<el-row type="flex" class="row-bg" justify="space-between">

  <el-col :span="2"><div class="grid-content">
      <el-button @click="toglMenu" icon="el-icon-more" circle></el-button></div></el-col>
  
  <el-col :span="6"><div class="grid-content">
    </div></el-col>
  
  <el-col :span="6"><div class="grid-content">
      <Search/></div></el-col>

  <el-col :span="1"><div class="grid-content">
      <el-dropdown>
        <i class="el-icon-s-tools" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>查看</el-dropdown-item>
          <el-dropdown-item>新增</el-dropdown-item>
          <el-dropdown-item>删除</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      </div></el-col>

  <el-col :span="6"><div class="grid-content">
      <User/>
    </div></el-col>

</el-row>
</div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css';
import User from '@/components/common/User.vue'
import Search from '@/components/common/Search.vue'

export default {
   name:"Header",
   components:{
       User,
       Search
   },
   methods: {
        toglMenu () {
            return this.$store.commit("toggleMenu");
        }
    },
}
</script>