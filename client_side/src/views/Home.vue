<template>
<div class="home">

  <Layout>
    <div class="list-wrapper">
    <VideoList listTitle="Featured"></VideoList>
    </div>
  </Layout>

</div>
</template>

<script>
import Layout from '@/views/Layout.vue'
import VideoList from '@/components/video/VideoList.vue'


export default {
  name: 'Home',

  components: {
    Layout,
    VideoList
  },
  methods: {
    
  }
}
</script>

<style>
.list-wrapper {
  padding-left: 5px;
}
</style>
