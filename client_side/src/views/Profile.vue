<template>
  <div>
    <div>
      <img :src="this.$auth.user.picture">
      <h2>{{ $auth.user.nickname }}</h2>
      <p>{{ $auth.user.email }}</p>
    </div>
    <div>
      <pre>{{ JSON.stringify($auth.user, null, 2) }}</pre>
    </div>

    <el-upload
        class="avatar-uploader"
        action=""
        :http-request="addAttachment"
        :auto-upload="true"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
      <img :src="imageUrl" class="avatar">
      <i class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>

    <div class="el-upload__tip" slot="tip">Only jpg/png files not exceeding 2MB allowed.</div>
    {{apiMessage}}

  </div>
</template>

<style scoped>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}
.avatar-uploader-icon {
  font-size: 30px;
  color: black;
  /*color: #8c939d;*/
  /*width: 120px;*/
  /*height: 120px;*/
  /*line-height: 60px;*/
  /*text-align: center;*/
  /*vertical-align:middle;*/
  position: absolute;
  top: 45px;
  left:45px;
}
.avatar {
  width: 120px;
  height: 120px;
  display: block;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      imageUrl: this.$auth.user.picture,
      apiMessage:''
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = (file.type === 'image/jpeg'|| 'image/png');
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('Sorry, only jpg/png files allowed :(');
      }
      if (!isLt2M) {
        this.$message.error('Sorry, try an image smaller than 2MB in size please :(');
      }
      return isJPG && isLt2M;
    },
    async addAttachment(file) {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      console.log(token)

      // Use Axios to make a call to the API
      const { data } = await axios.post('/api/profile_pic', file,
          {headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        }
      });

      this.apiMessage = data;
      // console.log("API called and fetched.");
    }
  }
}
</script>
