<template>
  <div>
    <div class="list-title">
      <h2>{{ listTitle }}</h2>
    </div>
    <el-row :gutter=15 v-infinite-scroll="getVideos" style="overflow:auto" class="card-tiles">
      <el-col :xs="12" :sm="8" :md="8" :lg="6" :xl="6" v-for="i in  loading? 10:14" :key="i" v-loading="loading">
        <VideoCard :video="video">
        </VideoCard>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import VideoCard from "@/components/video/VideoCard";
import VideoService from "@/services/VideoService";

export default {
  name: "VideoList",
  data() {
    return {
      loading: false,
      loaded: false,
      errored: false,
      videos: [],
      page: 1,

      video: {
        url: '/watch/12',
        thumbnail: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        title: 'Top western road trips Top western road trips Top western road trips Top western road trips',
        views: '9.6k',
        createdAt: '6 hours ago'
      },
    }
  },

  methods: {
    async getVideos($state) {
      // if(!this.loaded) {
      //   this.loading=true;
      // }
      //
      // const videos = await VideoService.getVideoList()
      //     .catch((err) => {
      //       console.log(err)
      //       this.errored = true
      //     })
      //     .finally(() => {
      //       this.loading = false
      //     })
      //
      // if (videos.data.data.length) {
      //   this.page += 1
      //   this.videos.push(...videos.data.data)
      //   $state.loaded()
      //   this.loaded = true
      // } else {
      //   $state.complete()
      // }
      console.log("1")
    },

  },
  components: {
    VideoCard
  },
  props: {
    listTitle: String
  }
}
</script>

<style scoped>
.list-title {
  /*margin-top: -15px;*/
  margin-left: 5px;
}
</style>