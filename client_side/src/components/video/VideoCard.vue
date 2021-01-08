<template>
  <!--<el-card @click="watch(video)">-->
  <el-card :body-style="{ padding: '0px' }" class="video-card">
    <div class="thumb">
      <el-image :src="video.thumbnail" router :to="video.url">
        <div slot="placeholder" class="image-slot">
<!--          <img src="/static/ui/placeholder_img.png"></img>-->
          <el-image :src="require('@/assets/ui/placeholder_img.png')"></el-image>
        </div>
      </el-image>
      <div class="card-layer">
        <div class="card-icon">
          <el-tooltip class="item" effect="dark" content="Watch Later" placement="left">
            <el-button type="info" icon="el-icon-time" size="small" circle></el-button>
          </el-tooltip>
        </div>
        <div class="video-time">

        </div>
      </div>
    </div>

    <div class="card-text">
      <div class="card-title" router :to="video.url">
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
      this.router.push("/video/" + video.id);
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
  opacity: 70%;
}

.card-title {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

</style>