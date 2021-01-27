<template>

    <!-- default-active="1-4-1" -->
    <el-menu class="el-menu-home" :collapse=true>
      <el-submenu class="el-submenu-home" index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">Home</span>
        </template>

        <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="1-1">选项1</el-menu-item>
        </el-menu-item-group>

        <el-submenu index="1-4">
          <span slot="title">选项4</span>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>

      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">Playlists</span>
      </el-menu-item>

    </el-menu>

</template>

<script>
export default {
  name: 'Menu',

  // methods: {
  //   handleOpen(key, keyPath) {
  //     console.log(key, keyPath);
  //   },
  //   handleClose(key, keyPath) {
  //     console.log(key, keyPath);
  //   }
  // }
}
</script>

<style>
.el-menu-home {
  height: 100vh;
}

/*.el-menu-home:not(.el-menu--collapse) {*/
/*  width: 200px;*/
/*  !*min-height: 400px;*!*/
/*}*/

.el-submenu-home {
  padding-top: 5px;
}
</style>
