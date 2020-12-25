<template>
<div class="home">
<el-container>
  <el-header>
      <Header/>
    </el-header>
  
  <el-container>
    <el-aside>
      <Menu/>
    </el-aside>
    
    <el-container>
    <el-main>Main</el-main>
    <el-footer>Footer</el-footer>
     </el-container>
  </el-container>

</el-container>

</div>
</template>

<script>
import Header from '@/components/common/Header.vue'
import Menu from '@/components/common/Menu.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Menu,
  },
  methods: {
    
  }
}
</script>
