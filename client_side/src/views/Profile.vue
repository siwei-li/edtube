<template>
  <Layout>
    <div class="wrapper">

      <div class="auth0">

        <div class="up-left">
          <div class="avatar-uploader">
            <el-upload
                action=""
                :http-request="addAttachment"
                :auto-upload="true"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload">
              <img :src="imageUrl" class="avatar">

              <div class="button-wrapper">
                <!--        <i class="el-icon-plus avatar-uploader-icon"></i>-->
                <el-button style="padding-left: 16px">Change Picture</el-button>
              </div>
            </el-upload>
          </div>
          <div class="upload-tip">(Only jpg/png files not exceeding 2MB allowed.)
          </div>

        </div>
        <div class="up-right">
          <el-form :inline="true" :model="auth0">
            <el-form-item label="Nickname:">
              <el-input v-model="auth0.nickname"></el-input>
              `
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="changeName">Change</el-button>
            </el-form-item>
          </el-form>
        </div>

      </div>

      <div>
        <h2>{{ $auth.user.nickname }}</h2>
        <p>{{ $auth.user.email }}</p>
        <pre>{{ JSON.stringify($auth.user, null, 2) }}</pre>
      </div>
      {{ apiMessage }}

    </div>
  </Layout>
</template>

<style scoped>
.wrapper {
  padding: 20px;
}

.avatar-uploader {
  width: 130px;
  height: 130px;
  border: 2px dashed #d9d9d9;
  border-radius: 10px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader:hover {
  border-color: #409EFF;
}

.button-wrapper {
  width: 130px;
  height: 130px;
  opacity: 50%;
  /*text-align: center;*/
  /*vertical-align:middle;*/
  /*line-height: 120px;*/
}

.button-wrapper:hover {
  opacity: 70%;
}

.avatar {
  width: 120px;
  height: 120px;
  display: block;
  position: absolute;
  top: 5px;
  left: 5px;
}

/*.avatar-uploader-icon {*/
/*  font-size: 40px;*/
/*  color: #8c939d;*/
/*  position: absolute;*/
/*  top: 45px;*/
/*  left:45px;*/
/*}*/
.upload-tip {
  margin-top: 5px;
  /*margin-left: -5px;*/
  /*width:150px;*/
  /*text-align: center;*/
  font-size: 12px;
}
</style>

<script>
import axios from "axios";
import Layout from "@/views/Layout";

export default {
  components: {Layout,},
  data() {
    return {
      auth0: {nickname: this.$auth.user.nickname},
      imageUrl: this.$auth.user.picture,
      apiMessage: ''
    };
  },
  methods: {
    changeName() {
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = (file.type === 'image/jpeg' || 'image/png');
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

