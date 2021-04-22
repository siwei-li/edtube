<template>
  <!--<el-card ">-->
  <el-card :body-style="{ padding: '0px' }" class="video-card">
    <div class="thumb">

      <div class="thumb-wrapper">
        <router-link :to="{ name: 'Watch',params:{id:video.id}}" target="_blank">
      <el-image :src='thumbSource + video.platform_id +"/hqdefault.jpg"' :lazy=true>
        <div slot="placeholder" class="image-slot">
          <!-- <img src="/static/ui/placeholder_img.png"> -->
          Loading<span class="dot">...</span>
        </div>
        <div slot="error" class="image-slot">
          <i class="el-icon-picture-outline"></i>
        </div>
      </el-image>
      </router-link>
      </div>

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
        <!-- <router-link :to="{ name: 'Watch',params:{id:video.id}}" target="_blank"> -->
        <span v-bind:title="video.title">{{ video.title }}</span>
        <!-- </router-link> -->
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
      loading:false,
      thumbSource:"https://i.ytimg.com/vi/",
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
      console.log(video);
      // this.$router.push('/watch/'+video.id);
      let routeData = this.$router.resolve({ name: 'Watch',params:{id:video.id}});
      window.open(routeData.href, '_blank');
    }
  }
}
</script>

<style lang="less" scoped>
.video-card {
  margin-bottom: 25px;
}

.thumb {
  position: relative;
}

.el-image {
  max-height: 100%;
  height: 200px;
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