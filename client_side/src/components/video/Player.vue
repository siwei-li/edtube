<template>
<el-row class="full-player" :gutter="20">
  <el-col :xs="24" :sm="16" :md="16" :lg="16" :xl="14" class="left-container">

    <div class="video-title">
      <h3>{{ video.title }}</h3>
    </div>

    <video controls>
      <source :src="video.videoUrl" type="video/mp4"/>
    </video>

    <el-card class="video-action" :body-style="{ padding: '10px'}">
      <el-row justify="space-between">

        <div>
          love Add to List
        </div>
      </el-row>
    </el-card>

  </el-col>

  <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="10">
    <div class="video-info">
      <el-collapse v-model="activeNames">
        <el-collapse-item name="info">
          <template slot="title">
            <div style="font-size: 18px">
              Info &nbsp<i class="el-icon-info"></i>
            </div>
          </template>
          <div class="video-description">{{ video.description }}</div>

          <!--          <el-divider></el-divider>-->
          <div class="video-time">
            <time>{{ video.createdAt }}</time>
          </div>
        </el-collapse-item>

      </el-collapse>

    </div>
  </el-col>
</el-row>
</template>

<script>
export default {
  name: "Player",
  data: () => ({
    loading: true,
    videoLoading: true,
    // truncate: true,
    activeNames: ['info']
  }),
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  methods: {

    // show(event) {
    //   if (event.target.innerText === 'SHOW MORE') {
    //     this.truncate = false
    //     event.target.innerText = 'SHOW LESS'
    //   } else {
    //     this.truncate = true
    //     event.target.innerText = 'SHOW MORE'
    //   }
    // },
    // truncateText(string = '', num) {
    //   if (string.length <= num) {
    //     return string
    //   }
    //   return string.slice(0, num)
    // },

  },

  mounted() {
    this.loading = false
    this.videoLoading = false
  }
}
</script>

<style>
.left-container {
  /*padding-right: 15px;*/
}

.video-title h3 {
  margin: 10px 5px;
  font-size: 18px;
  font-family: Roboto Arial sans-serif;
}

video {
  /*max-width: 100%;*/
  /* min-height: 360px;*/
  /*width: 704px;*/
  /*height: 396px;*/
  width: 100%;
  margin-bottom: -5px;
  /*min-width: 100%;*/
}

.video-info {
  margin-left: 5px;
}

.video-description {
  max-height: 396px;
  /*overflow-y: scroll;*/
  overflow-y: auto;
  padding-right: 15px;
}

.video-time {
  font-size: 14px;
  padding-top: 15px;
}
</style>