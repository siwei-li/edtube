<template>
  <!--<el-card ">-->
  <el-card :body-style="{ padding: '0px' }" class="video-card">
    <div class="thumb">
      <el-image :src="video.thumbnail" @click="watch(video)">
        <div slot="placeholder" class="image-slot">
          <!--          <img src="/static/ui/placeholder_img.png"></img>-->
          <el-image :src="require('@/assets/ui/placeholder_img.png')"></el-image>
        </div>
      </el-image>
      <div class="card-layer">
        <div class="card-icon">
          <el-tooltip class="item" effect="dark" content="Watch Later" placement="left">
            <el-button type="info" class="custom-icon" icon="el-icon-time" size="small"></el-button>
          </el-tooltip>
        </div>
        <div class="video-time">

        </div>
      </div>
    </div>

    <div class="card-text">
      <div class="card-title" @click="watch(video)">
        <span v-bind:title="video.title">{{ video.title }}</span>
      </div>
      <div class="card-info">
        details
      </div>
    </div>

  </el-card>
</template>

<script>
export default {
  name: "VideoCard",
  data() {
    return {

    };
  },
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  methods: {
    watch(video) {
      this.$router.push(video.url);
    }
  }
}
</script>

<style scoped>
.video-card {
  margin-bottom: 25px;
}

.thumb {
  position: relative;
}

.card-layer {
  position: absolute;
  top: 5px;
  right: 5px;
  opacity: 80%;
}

.custom-icon {
  font-size: 20px;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-title {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

</style>