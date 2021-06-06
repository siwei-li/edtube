<template>
  <div class="article-edit">
    <div class="content-main">
      <div class="content-wrapper">
        <el-row>
          <el-col :span="18" :offset="4">
            <el-card>
              <p class="data-title">直播中心</p>
              <el-row :gutter="20">
                <el-col :span="4">
                  <el-menu
                      default-active="1-1"
                      class="el-menu-vertical-demo"
                      @open="handleOpen"
                      @close="handleClose"
                      :unique-opened="true"
                      text-color="black"
                      active-text-color="#ffd04b"
                      menu-trigger="click"
                      @select="handleSelect"
                  >
                    <el-submenu index="1">
                      <template slot="title">
                        <i class="el-icon-location"></i>
                        <span>直播操作台</span>
                      </template>
                      <el-menu-item-group>
                        <!-- 数据展示X轴 时间  Y轴 人数 -->
                        <el-menu-item index="1-1">直播数据</el-menu-item>
                        <el-menu-item index="1-2">申请中心</el-menu-item>
                        <el-menu-item index="1-3">直播间</el-menu-item>
                      </el-menu-item-group>
                      <!-- <el-submenu index="1-4">
                <template slot="title">选项4</template>
                <el-menu-item index="1-4-1">选项1</el-menu-item>
                      </el-submenu> -->
                    </el-submenu>
                  </el-menu>
                </el-col>
                <el-col :span="18" :offset="2">
                  <el-card>
                    <div class="OnlineD">
                      <el-card v-show="status === '1-1'" class="card">
                        <p class="data-title">直播数据</p>
                        <div class="chart_wrapper" id="video_sum"></div>
                      </el-card>
                      <el-card v-if="status === '1-2'" class="card">
                        <p class="data-title">申请信息</p>
                        <p v-show="!applyStatus" class="applyTitle">您已认证成功，赶快去直播吧!</p>
                        <p v-show="applyStatus" class="applyTitle">实名认证成功后,可以享受开通直播间等服务!</p>
                        <el-form
                            ref="form"
                            :model="form"
                            :rules="formRule"
                            label-position="left"
                            label-width="80px"
                            v-show="applyStatus"
                        >
                          <el-form-item label="真实姓名" prop="name">
                            <el-input v-model="form.name"></el-input>
                          </el-form-item>
                          <el-form-item label="证件类型" prop="type">
                            <el-select v-model="form.type" placeholder="请选择证件类型">
                              <el-option label="身份证" value="1"></el-option>
                              <el-option label="护照（中国签发）" value="2"></el-option>
                              <el-option label="其他国家或地区证明" value="3"></el-option>
                            </el-select>
                          </el-form-item>
                          <el-form-item label="证件号码" prop="number">
                            <el-input v-model.number="form.number"></el-input>
                          </el-form-item>
                          <el-form-item label="证件上传">
                            <el-upload
                                class="avatar-uploader"
                                :action="$store.state.host+'/profile/pic/'+6"
                                :show-file-list="false"
                                :on-success="handleAvatarSuccess"
                                :before-upload="beforeAvatarUpload"
                            >
                              <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                            </el-upload>
                          </el-form-item>
                          <el-form-item>
                            <el-button
                                class="buttonC"
                                type="primary"
                                @click="submitForm('form')"
                            >提交认证</el-button>
                          </el-form-item>
                        </el-form>
                      </el-card>
                      <el-card v-if="status === '1-3'" class="card">
                        <p class="data-title">发起直播</p>
<!--                        <OnlineRoom/>-->
                      </el-card>
                    </div>
                  </el-card>
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
// import OnlineRoom from "./OnlineRoom.vue"

export default {
  name: "Live",
  // components:{ OnlineRoom },
  data() {
    return {
      //用于控制展示的card展示的内容
      status: "1-1",
      //用于控制申请状态的隐藏显示
      applyStatus: true,
      form: {
        name: "",
        type: "",
        number: ""
      },
      imageUrl: "",
      postFilel: "",
      formRule: {
        name: [
          { required: true, message: "请输入真实姓名", trigger: "blur" },
          { min: 3, max: 5, message: "长度在 3 到 5 个字符", trigger: "blur" }
        ],
        type: [
          { required: true, message: "请选择证件类型", trigger: "change" }
        ],
        number: [
          { required: true, message: "证件号码不能为空" },
          { type: 'number', message: '证件号码必须为数字值'}
        ],
        date1: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ],
        array: {
          type: "array",
          required: true,
          message: "请至少选择一个活动性质",
          trigger: "change"
        }
      }
    };
  },
  mounted() {
    // this.getHbase();
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log('可以执行申请相关提交')

          // 此处的传值都为formData
          var fileData  = new FormData()
          fileData.append('firstFile',file)
          // 最终提交的所有字段都为
          fileData.append('name',this.form.name)
          fileData.append('type',this.form.type)
          fileData.append('number',this.form.number)
          fileData.append('postFilel',this.postFilel)
          this.$axios({
            method: 'post',
            url: '0.0.0.0.',
            data:fileData
          }).then(res =>{
            if(res.code === 200){
              // 执行相关的操作
              this.applyStatus = false
            }
          })
        } else {
          console.log("请输入完整信息");
          this.$message({
            message: '请完成表单信息',
            type: 'warning'
          })
          return false;

        }
      });
    },
    handleAvatarSuccess(res, file) {
      console.log(file);
      this.imageUrl = URL.createObjectURL(file.raw);
      this.postFilel = file;
    },
    beforeAvatarUpload(file) {
      console.log("file");
      console.log(file);
      const isJPG = file.type === "image/jpeg" || file.type === "image/png";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG/PNG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },

    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleSelect(key, keyPath) {
      console.log(keyPath);
      console.log(key);
      this.status = key;
    },
    getLine() {
      let option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow"
          },
          formatter: "{b} : 在线{c}人"
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "10%",
          containLabel: true
        },
        xAxis: {
          type: "category",
          data: this.x_data
        },
        yAxis: {
          type: "value",
          axisLabel: {
            formatter: "{value} 人"
          }
        },
        series: [
          {
            data: this.y_data,
            type: "bar"
          }
        ]
      };
      let myChart = this.$echarts.init(document.getElementById("video_sum"));
      myChart.setOption(option);
      window.addEventListener("resize", function() {
        myChart.resize();
      });
    },
    getHbase() {
      this.$axios({
        method: "get",
        url: "/video/hbase",
        params: {}
      }).then(res => {
        console.log(res);
        if (res.code === 200) {
          this.x_data = res.data.counts_x_data;
          this.y_data = res.data.counts_y_data;
          this.getLine();
        } else {
          this.$message({
            message: "获取数据失败",
            type: "warning"
          });
        }
      });
    }
  }
};
</script>

