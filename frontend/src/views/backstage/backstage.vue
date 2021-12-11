<template>
  <div class=dynamic>
      <div class="back-header">
      <mu-appbar title='后台'>
        <mu-icon-button icon="chevron_left" slot="left" @click="goback" />
        <mu-icon-button icon="expand_more" slot="right"/>
      </mu-appbar>
    </div>
    <table border="1" class="lebt">
  <caption class = cap>撤回消息</caption>
  <tr>
    <th>用户名</th>
    <th>消息</th>
    <th>时间</th>
  </tr>
  <tr v-for="obj in getwithdrawMessages" :key = obj.id>
    <td>{{ obj.username }}</td>
    <td>{{ obj.msg }}</td>
    <td>{{ obj.gentime }}</td>
  </tr>
</table>

    <table border="1" class="lebt">
  <caption class = cap>用户反馈</caption>
  <tr>
    <th>用户名</th>
    <th>反馈内容</th>
    <th>时间</th>
  </tr>
  <tr v-for="obj in getfeedbacks" :key = obj.id>
    <td>{{ obj.username }}</td>
    <td>{{ obj.content }}</td>
    <td>{{ obj.gentime }}</td>
  </tr>
</table>
  </div>
</template>

<script>
// import faker from 'faker'
import { mapGetters } from 'vuex'
import { getUserName } from '@/utils/localStorage'

export default{
  data () {
    return {
      name: '',
      chatMsg: '',
      container: {},
      avatar: '/static/images/avatar1.jpg'
    }
  },
  created () {
    const username = getUserName()
    if (!username) {
      // 防止未登录
      this.$router.push({path: '/login'})
    }
    this.name = username
    // this.$store.dispatch('SetWebSocket', new WebSocket('ws://localhost:9090/mydynamics/'))
  },
  mounted () {
    this.container = document.querySelector('.chat-content')
    const that = this
    // 初始化新的对话信息
    this.$store.dispatch('SetChatMsg')
    // 加载历史对话信息
    this.$store.dispatch('GetWithdrawmessages')
    this.$store.dispatch('GetFeedbacks')
    // 自动滚动到底部
    setTimeout(() => {
      this.$nextTick(() => {
        this.container.scrollTop = 10000
      })
    }, 1000)
    this.getSocket.onmessage = (message) => {
      let receivedMsg = JSON.parse(message.data)
      console.log(receivedMsg)
      const now = new Date()
      const msgData = {
        'username': receivedMsg.username,
        'msg': receivedMsg.msg,
        'gentime': now.toISOString()
      }
      that.$store.dispatch('AddChatMsg', msgData)
    }
  },
  methods: {
    goback () {
      // 返回时断开连接
      this.$store.dispatch('SetWebSocket', null)
      this.$router.goBack()
    },
    // send () {
    //   const now = new Date()
    //   const msgData = {
    //     'username': this.name,
    //     'msg': this.chatMsg,
    //     'gentime': now.toISOString()
    //   }
    //   this.$store.dispatch('AddMessHistory', msgData)
    //   this.$store.dispatch('AddChatMsg', msgData)
    //   this.getSocket.send(JSON.stringify(msgData))
    //   this.chatMsg = ''
    // },
    scrollToBottom () {
      let container = document.querySelector('.chat-content')
      let scrollHeight = container.scrollHeight
      container.scrollTop = scrollHeight
    }
    // del () {
    //   console.log('delete')
    //   this.$store.dispatch('DelChatMsg', msgData)
    // }
  },
  computed: {
    ...mapGetters([
      'getSocket',
      'getUsers',
      'getInfo',
      'getMsgHistoryInfo',
      'getDynamicsHistoryInfo',
      'getfeedbacks',
      'getwithdrawMessages'
    ])
  },
  updated () {
    this.scrollToBottom()
  }
}
</script>

<style scope>
.dynamic{
   color: #000;
}
.back-header {
  position: fixed;
  height: 50px;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1;
}
.lebt {
    position: relative;
    top: 70px;
    margin:auto;
}
.cap {
    font-size: x-large;
    font-weight: bold;
}
</style>
