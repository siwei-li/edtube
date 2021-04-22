<template>
  <div class="watch">
    <Layout>
    
      <Player v-if="!videoLoading" :video="video"></Player>


      <el-row :gutter="20">
        <el-col :xs="24" :sm="16" :md="16" :lg="16" :xl="14">
          <Comment :commentList="commentList"></Comment>
        </el-col>
        <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="10">
          <Recommend></Recommend>
        </el-col>
      </el-row>

    </Layout>
  </div>
</template>

<script>
import Player from "@/components/video/Player";
import Layout from "@/views/Layout";
import Comment from "@/components/comment/Comment";
import Recommend from "@/components/recommend/Recommend";

import VideoService from "@/services/VideoService";

export default {
  name: "Watch",
  data() {
    return {
      loading: false,
      videoLoading:true,
      loaded: false,
      errored: false,
      videos: [],
      page: 1,
      video:{},
       commentList: [
        {
          id: "111",
          nickName: "chloe",
          replyData: "lallla",
          good: 100,
          bad: 1,
          showTextarea: false,
          timestamp: 1600670910515,
          replyList: [
            {
              id: "111",
              nickName: "tom",
              toUser: "chloe",
              replyData: "大师兄说的对",
              good: 2,
              bad: 0,
              showTextarea: false,
              textarea: "",
              timestamp: 1600670910515,
            },
          ],
        },
        {
          id: "222",
          nickName: "jeny",
          good: 500,
          bad: 9,
          replyData: "好棒哇哇哇哇哇",
          showTextarea: false,
          replyList: [],
          timestamp: 1600670910515,
        },
      ],

    }
  },
  mounted() {
    this.getVideo(this.$route.params.id);
  },
  methods: {
    async getVideo(id) {
      this.errored = false
      this.videoLoading = true
      this.video = {}
      try {
        const video = await VideoService.getVideo(id)

        // if (!video) return this.$router.push('/')
        this.video = video.data.data
        console.log(this.video)
      } catch (err) {
        this.errored = true
        console.log(err)
      } finally {
        this.videoLoading = false
        // this.checkSubscription(this.video.userId._id)
        // this.checkFeeling(this.video._id)
      }
    //   if (this.currentUser && this.currentUser._id === this.video.userId._id) {
    //     this.showSubBtn = false
    //   } else {
    //     this.showSubBtn = true
    //   }

    //   if (!this.isAuthenticated) return

    //   if (
    //     this.video.userId._id.toString() !== this.currentUser._id.toString() &&
    //     this.video.status !== 'public'
    //   )
    //     return this.$router.push('/')

    //   const data = {
    //     type: 'watch',
    //     videoId: this.video._id
    //   }

    //   await HistoryService.createHistory(data).catch((err) => console.log(err))
    // },

  },
  },
  components: {
    Layout, Player, Comment, Recommend
  },

}
</script>

<style scoped>
.watch {
  padding-left: 5px;
}
</style>