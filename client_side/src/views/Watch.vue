<template>
  <div class="watch">
    <Layout>
      <Player :video="video"></Player>

      <el-row :gutter="20">
        <el-col :xs="24" :sm="16" :md="16" :lg="16" :xl="14">
          <Comment :commentList="commentList"></Comment>
        </el-col>
        <el-col :xs="24" :sm="8" :md="8" :lg="8" :xl="10">
          <Recommend></Recommend>
        </el-col>
      </el-row>

    </Layout>
  </div>
</template>

<script>
import Player from "@/components/video/Player";
import Layout from "@/views/Layout";
import Comment from "@/components/comment/Comment";
import Recommend from "@/components/recommend/Recommend";

export default {
  name: "Watch",
  components: {Recommend, Comment, Layout, Player},
  data: () => ({
    video: {},
    commentList: [
      {
        id: "111",
        nickName: "chloe",
        replyData: "lallla",
        good: 100,
        bad: 1,
        showTextarea: false,
        timestamp: 1600670910515,
        replyList: [
          {
            id: "111",
            nickName: "tom",
            toUser: "chloe",
            replyData: "大师兄说的对",
            good: 2,
            bad: 0,
            showTextarea: false,
            textarea: "",
            timestamp: 1600670910515,
          },
        ],
      },
      {
        id: "222",
        nickName: "jeny",
        good: 500,
        bad: 9,
        replyData: "好棒哇哇哇哇哇",
        showTextarea: false,
        replyList: [],
        timestamp: 1600670910515,
      },
    ],

  }),
  methods: {
    getVideos() {
      this.video = {
        channelName: 'Tech Reagan',
        subscribers: '100k',
        createdAt: '2021-01-19',
        // videoUrl: '/video.mp4',
        videoUrl: "https://www.youtube.com/embed/VhtFSSq3lXo",
        title: 'Attendance Management System Attendance Management System Attendance Management System Attendance Ma',
        description:
            'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Culpa vel inventore voluptatum reiciendis delectus quibusdam incidunt consequuntur, nostrum aperiam, natus quidem qui corrupti reprehenderit quaerat neque voluptatibus? Ullam, maiores temporibus!'
            + '♪♫♪ ♪♫♫♪ \n' +
            '\n' +
            'This is a continuation of my old account from 6 years ago (rareviolintreasures), I started running out of things to upload that were out of print or rare and was just too tired to continue because I was working in excess of 100 hour weeks. My intention was to get the majority of recordings I had that were difficult to find, once I felt I had accomplished this goal, I decided it was time to stop. \n' +
            '\n' +
            'A few months later I somehow got locked out of my account so 6 years later I am ready to resume. It was my hope that many collectors would continue where I left off and I\'m amazed and delighted to see how many recordings have been made public in my absence.\n' +
            '\n' +
            'I have always encouraged sharing out of print recordings but it is upsetting to see recordings made public of recordings that are still commercially available. Alot has changed in my 6 year absence as some things that were in print no longer are and vice versa, so keep in mind I no longer have access to my old account and can not modify or delete anything I put up before, it has always been my intention to not share recordings that still are in print as this would reduce support for the artist. It is my intention to only share music that is no longer commercially in print as I am as respectful as I can be to artists and record companies that continue to make their art available to fans like me. My intention is to share recordings to make recordings available so they do not get lost or forgotten. It is also my wish to share recordings for fans like me but also for the purpose of those who study the violin and encourage all who listen to acquire their own personal copy of these recordings in the used cd/lp market, in other words even though you hear it here on you tube for free, get your own legitimate copy if you hear something you like. I also would like to encourage others to fill in the gaps and pick up where I let off with recordings I don\'t have or may have missed, but only if the recordings have gone out of print. I want to re-emphasize I discourage anyone to upload a recording if it is still being sold commercially.\n' +
            '\n' +
            '♪♫♪ ♪♫♫♪'
      }
    },
  },
  mounted() {
    setTimeout(() => {
      this.getVideos()
    }, 400)
  }
}
</script>

<style scoped>
.watch {
  padding-left: 20px;
}
</style>