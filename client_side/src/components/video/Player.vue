<template>
  <el-row class="full-player" :gutter="20">
    <el-col :xs="24" :sm="16" :md="16" :lg="16" :xl="14" class="left-container">

      <div class="video-title">
        <h3>{{ video.title }}</h3>
      </div>

      <vue-plyr ref="plyr">
        <div data-plyr-provider="youtube" data-plyr-embed-id="bTqVqk7FSmY"></div>
      </vue-plyr>

      <!--    <vue-plyr ref="plyr">-->
      <!--      <div class="plyr__video-embed">-->
      <!--        <iframe-->
      <!--            :src="video.videoUrl+'?amp;iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1'"-->
      <!--            allowfullscreen-->
      <!--            allowtransparency-->
      <!--            allow="autoplay"-->
      <!--        ></iframe>-->
      <!--      </div>-->
      <!--    </vue-plyr>-->

      <el-card class="video-action" :body-style="{ padding: '10px'}">
        <el-row type="flex" justify="space-between">

          <div id="icons">
            <div id="like" v-on:click="toglLike">
              <img v-if="liked" src="../../assets/images/videoDetail/like-active.png">
              <img v-else src="../../assets/images/videoDetail/like-default.png">
              <span>&nbsp;Like</span>
            </div>
            <div id="save" v-on:click="toglSave">
              <el-button v-if="saved" type="primary" class="custom-icon" icon="el-icon-star-off" circle
                         size="small"></el-button>
              <el-button v-else type="warning" class="custom-icon" icon="el-icon-star-on" circle
                         size="small"></el-button>
              <span>&nbsp;Save</span>
            </div>
            <div>
              <span>Subscribe</span>
            </div>
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
    activeNames: ['info'],
    timer: '',
    timeStamp: 0,
    timePlayed: 0,
    energyPoint: 0,
    liked: 0,
    saved: 0,
  }),
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  methods: {
    timing() {
      this.timer = setInterval(this.setEnergy, 7000)
    },
    getLapse() {
      this.timePlayed += (this.$refs.plyr.player.currentTime - this.timeStamp);
      this.timeStamp = this.$refs.plyr.player.currentTime;
      return this.timePlayed;
    },
    setEnergy() {
      console.log(Math.round(1.7 * this.getLapse()))
    },
    toglLike() {
      this.liked = 1 - this.liked;
    },
    toglSave() {
      this.saved = 1 - this.saved;
    }
  },

  mounted() {
    this.loading = false
    this.videoLoading = false
    // console.log(this.$refs.plyr.player)
    this.$refs.plyr.player.on('ready', this.timing)
  },
  beforeDestroy() {
    console.log(this.timePlayed);
    clearInterval(this.timer);
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

/*video {*/
/*  !*max-width: 100%;*!*/
/*  !* min-height: 360px;*!*/
/*  !*width: 704px;*!*/
/*  !*height: 396px;*!*/
/*  width: 100%;*/
/*  margin-bottom: -5px;*/
/*  !*min-width: 100%;*!*/
/*}*/
iframe {
  border: none;
  width: 100%;
  height: 396px;
  margin-bottom: -5px;
}

#icons {
  display: flex;
  align-items: center;
}

#like {
  display: flex;
  align-items: center;
  margin-right: 8px;
}

#save {
  display: flex;
  align-items: center;
}

.video-action img {
  width: 25px;
  margin-right: 5px;
}

.custom-icon {
  margin-right: 5px;
  margin-top: -2px;
  font-size: 20px;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-info {
  margin-left: 5px;
}

.video-description {
  /*max-height: 432px;*/
  max-height: 70vh;
  /*overflow-y: scroll;*/
  overflow-y: auto;
  padding-right: 15px;
}

.video-time {
  font-size: 14px;
  padding-top: 15px;
}
</style>