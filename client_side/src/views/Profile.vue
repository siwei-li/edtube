<template>
  <Layout>
    <div class="wrapper">

      <div class="auth0">

        <div class="up-left">
          <div class="avatar-uploader">
            <el-upload
                action=""
                :show-file-list="false"
                :http-request="upload"
                :auto-upload="true"
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
          <el-form :inline="true" :model="form">
            <el-form-item label="Nickname:">
              <el-input v-model="prefill"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="changeName">Change</el-button>
            </el-form-item>
          </el-form>
        </div>

      </div>

<!--      <div>-->
<!--        <h2>{{ $auth.user.nickname }}</h2>-->
<!--        <p>{{ $auth.user.email }}</p>-->
<!--        <pre>{{ JSON.stringify($auth.user, null, 2) }}</pre>-->
<!--      </div>-->
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
import Layout from "@/views/Layout";
import ProfileService from "@/services/ProfileService";

export default {
  components: {Layout,},
  data() {
    return {
      imageUrl: this.$auth.user.picture,
      apiMessage: 'init',
      form: {Nickname:''},
      prefill:this.$auth.user.nickname,
    };
  },
  methods: {
    async changeName() {
      const object = {"nickname":this.prefill};
      console.log(JSON.stringify(object))
      try {
      const response = await ProfileService.updateNickname(JSON.stringify(object)
      )
      // , {headers: {
      //     Authorization: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFGcW9LcXFfVEVQYkxKX0R0eVVITCJ9.eyJpc3MiOiJodHRwczovL2VkdHViZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmNzJlOWQ1NGVhMjAwMDY5Yzg4NmQ5IiwiYXVkIjpbImh0dHBzOi8vZWR0dWJlIiwiaHR0cHM6Ly9lZHR1YmUudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxODg5MDMyNCwiZXhwIjoxNjE4OTc2NzI0LCJhenAiOiJoSTkzaVBHTTl4NHduYmVSeFNuMENwb2lPR0JFYXNTcSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJwZXJtaXNzaW9ucyI6W119.K3tPNrloQzKJ5fMHAcgR1wTbFySn0pWdV5XjVO-hsv2Xl2Y_94ntPP8pwBs3AXw7Q-1F6nEWxWP_Z3kLNf_jNNCbx6EDGOu6usZRZDggFAFJi1bsKNp5mmgtYEjIl6AEVVJ9V6qyA_UKSIrFZcVqPJLkjpNlnsS92iEuLIMMcy4gYeHpWGocH_w0Td15zIRcbjpi5OIoJi0mMFczgKP_AHyZmC2is8XLsqmALnNpaJCiCp9pVugwpY7gxWmc-8ESWb_056fGDMTyimaTTjSvgn7RaBGV6KlfZyC5i1qTlFqWO57fY-DMWPtRQIZIiv8WCfC9kR0fSk3xQtrevGGupA`
      //   }})
      this.apiMessage = response;
      } catch (err) {
        console.log(err)
      }
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

    async upload(file) {
      const { data } = await ProfileService.profilePic(file);
      this.apiMessage = data;
      // console.log("API called and fetched.");
    }
  }
}
</script>

