<template>
  <div class=dynamic>
    <div v-for="obj in getDynamicsHistoryInfo" :key="obj.id">
        <dynamics :id="obj.id" :content="obj.content" :username="obj.username" :mytime="obj.gentime" :comments="obj.comments">
        </dynamics>
    </div>
  </div>
</template>

<script>
// import faker from 'faker'
import { mapGetters } from 'vuex'
import Dynamics from '../../components/Dynamics'
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
    this.$store.dispatch('SetWebSocket', new WebSocket('ws://localhost:9090/chat/'))
  },
  mounted () {
    // this.container = document.querySelector('.chat-content')
    const that = this
    // 初始化新的对话信息
    this.$store.dispatch('SetChatMsg')
    // 加载历史对话信息
    this.$store.dispatch('GetDynamicsHistory')
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
      'getDynamicsHistoryInfo'
    ])
  },
  updated () {
    this.scrollToBottom()
  },
  components: {
    'Dynamics': Dynamics
  }
}
</script>

<style scoped>
.dynamic{
   color: #000;
}

</style>
