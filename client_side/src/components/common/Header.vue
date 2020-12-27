<template>
<div>
<el-row type="flex" class="row-bg" justify="space-between">

  <el-col :span="2">
    <div class="togl">
      <el-button @click="toglMenu" icon="el-icon-more" circle></el-button>
    </div>
  </el-col>
  
  <el-col :span="6"><div class="grid-content">
    </div></el-col>
  
  <el-col :span="6"><div class="search">
      <Search/>
  </div></el-col>

  <el-col :span="1"><div class="grid-content">
      <el-dropdown>
        <i class="el-icon-s-tools" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>查看</el-dropdown-item>
          <el-dropdown-item>新增</el-dropdown-item>
          <el-dropdown-item>删除</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      </div>
  </el-col>

  <el-col :span="6"><div class="user">
      <User/>
    </div>
  </el-col>

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

<style lang="less" scoped>
// 使用了字体图标，直接在父元素上面加font-size不起作用
// 用到 less 预编译的深度作用选择器  /deep/
// 当前 原生的是  >>>
//.el-button {
//  width: 80px;
//  height: 80px;
//  padding: 0;
//  /deep/ i {
//    font-size: 30px;
//  }
//}

</style>