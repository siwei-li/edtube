<template>
  <div class="menu-wrapper">

    <!-- default-active="1-4-1" -->
    <el-menu class="el-menu-home" :collapse="isCollapsed">
      <el-submenu class="el-submenu-home" index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">Home</span>
        </template>

        <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="1-1">选项1</el-menu-item>
        </el-menu-item-group>

        <el-submenu index="1-4">
          <span slot="title">选项4</span>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>

      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">Playlists</span>
      </el-menu-item>

    </el-menu>

  </div>
</template>

<script>
export default {
  data() {
    return {
      // isCollapsed: true
      navData: [
        {
          index: "/article",
          title: "内容",
          icon: "el-icon-location",
          second: [
            {
              title: "这里全是知识库相关",
              child: [
                {
                  index: "/article/list",
                  content: "知识文章"
                },
                {
                  index: "/article/sort",
                  content: "分类管理"
                },
                {
                  index: "/article/organize",
                  content: "机构管理"
                },
                {
                  index: "/article/comment",
                  content: "评论管理"
                },
                {
                  index: "/article/report",
                  content: "举报管理"
                }
              ]
            }
            // {
            //     third: [
            //         {
            //             title: "举报相关",
            //             index: "",
            //             child: [
            //                 {
            //                     index: "",
            //                     content: "已举报"
            //                 },
            //                 {
            //                     index: "",
            //                     content: "已举报"
            //                 }
            //             ]
            //         }
            //     ]
            // }
          ]
        },
        {
          index: "/hospital",
          title: "医院医生",
          icon: "el-icon-menu",
          second: [
            {
              title: "医院医生相关信息",
              child: [
                {
                  index: "/hospital/hospitalList",
                  content: "医院库"
                },
                {
                  index: "/hospital/doctorList",
                  content: "医生库"
                },
                {
                  index: "/hospital/doctorTeamList",
                  content: "团队医生"
                },
                {
                  index: "/hospital/doctorApply",
                  content: "申请入住"
                }
              ]
            }
          ]
        },

        // {
        //     index: "3",
        //     title: "医生问答",
        //     icon: "el-icon-menu",
        //     second: []
        // },
        // {
        //     index: "4",
        //     title: "申请入住",
        //     icon: "el-icon-menu",
        //     second: []
        // },
        // {
        //     index: "5",
        //     title: "患者列表",
        //     icon: "el-icon-menu",
        //     second: []
        // },
        {
          index: "/community",
          title: "社区管理",
          icon: "el-icon-menu",
          second: [
            {
              child: [
                {
                  index: "/community/circleList",
                  content: "圈子列表"
                },
                {
                  index: "/community/invitationList",
                  content: "帖子列表"
                },
                {
                  index: "/community/commentList",
                  content: "评论列表"
                },
                {
                  index: "/community/report",
                  content: "举报管理"
                }
              ]
            }
          ]
        },
        // {
        //     index: "7",
        //     title: "评论审批",
        //     icon: "el-icon-menu",
        //     second: []
        // },
        {
          index: "8",
          title: "活动设置",
          icon: "el-icon-menu",
          second: [
            {
              child: [
                {
                  index: "/activity/banner",
                  content: "banner设置"
                }
              ]
            }
          ]
        },
        {
          index: "/shop",
          title: "商品管理",
          icon: "el-icon-menu",
          second: [
            {
              child: [
                {
                  index: "/shop/list",
                  content: "商品列表"
                }
              ]
            }
          ]
        },
        {
          index: "10",
          title: "订单信息",
          icon: "el-icon-menu",
          second: [
            {
              child: [
                {
                  index: "/order/list",
                  content: "订单列表"
                }
              ]
            }
          ]
        }
      ]
    };
  },
  computed: {
    isCollapsed() {
      return this.$store.state.menuCollapsed
    }
  },

  // methods: {
  //   handleOpen(key, keyPath) {
  //     console.log(key, keyPath);
  //   },
  //   handleClose(key, keyPath) {
  //     console.log(key, keyPath);
  //   }
  // }
}
</script>

<style>
.el-menu-home {
  height: 100vh;
}

.el-menu-home:not(.el-menu--collapse) {
  width: 200px;
  /*min-height: 400px;*/
}
.el-submenu-home {
  padding-top: 5px;
}
</style>
