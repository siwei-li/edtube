<template>
  <div>
    <div class="list-title">
      <h2>{{ listTitle }}</h2>
    </div>
    <el-row :gutter=15 v-infinite-scroll="getVideos" style="overflow:auto" class="card-tiles">
      <el-col :xs="24" :sm="8" :md="6" :lg="6" :xl="6"
              v-for="(video, i) in  videos" :key="i"
      v-loading="loading">
        <!--              loading ? 12 :-->
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
      video:{}

    }
  },
  mounted() {
    this.getVideos();
  },
  methods: {
    async getVideos($state) {
      if(!this.loaded) {
        this.loading=true;
      }

      const videos = await VideoService.getVideoList({page:this.page})
          .catch((err) => {
            console.log(err)
            this.errored = true
          })
          .finally(() => {
            this.loading = false
          })

      if (typeof videos === 'undefined') return
      console.log(videos.data)
      if (videos.data.results.length) {
        this.page += 1
        this.videos.push(...videos.data.results)
        console.log(this.videos)
        // $state.loaded()
        this.loaded = true
      } else {
        // $state.complete()
      }
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