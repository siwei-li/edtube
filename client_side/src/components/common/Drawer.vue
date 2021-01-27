<template>
  <el-drawer
      title="EdTube"
      :visible.sync="drawer"
      :before-close="handleClose"
      :direction="direction"
      size="300px">

    <div>我来啦!</div>
  </el-drawer>
</template>

<script>
export default {
  name: "Drawer",
  data() {
    return {
      // drawer: true,
      direction: 'ltr',
    };
  },
  computed: {
    drawer() {
      return this.$store.state.drawer;
    }
  },
  methods: {
    handleClose() {
      return this.$store.commit("toggleMenu");
    }
  }
}
</script>

<style scoped>

</style>