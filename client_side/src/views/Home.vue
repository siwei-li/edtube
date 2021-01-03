<template>
<div class="home">

  <Layout>
    <VideoList></VideoList>
  </Layout>

</div>
</template>

<script>
import Layout from '@/views/Layout.vue'
import VideoList from '@/components/VideoList.vue'


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
