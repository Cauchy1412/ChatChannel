<template>
  <div>
    <div class="content-list">
      <mu-list>
        <mu-sub-header>最近聊天记录</mu-sub-header>
        <mu-list-item title="聊天室" to='/chat' >
          <mu-avatar src="/static/images/avatar1.jpg" slot="leftAvatar" />
          <mu-icon value="chat_bubble" slot="right"/>
        </mu-list-item>
      </mu-list>
    </div>
    <div class="footer-nav">
      <mu-bottom-nav :value="bottomNav" @change="handleChange">
      <mu-bottom-nav-item value="home" title="主页" icon="restore" to='/' />
      <mu-bottom-nav-item value="me" title="个人中心" icon="favorite" to='/me' />
      <mu-bottom-nav-item value="about" title="关于" icon="location_on" to='/about' />
      <mu-bottom-nav-item value="mydynamics" title="动态" icon="favorite" to='/mydynamics' />
      <mu-bottom-nav-item v-if="name == 'admin'" value="backstage" title="后台" icon="restore" to='/backstage' />
    </mu-bottom-nav>
    </div>
  </div>
</template>

<script>
import { getUserName } from '../../utils/localStorage'
export default{
  data () {
    return {
      name: '',
      bottomNav: 'home'
    }
  },
  created () {
    const username = getUserName()
    if (!username) {
      // 防止未登录
      this.$router.push({path: '/login'})
    }
    this.name = username
    // this.$store.dispatch('SetWebSocket', new WebSocket('ws://localhost:9090/chat/'))
  },
  methods: {
    handleChange (val) {
      this.bottomNav = val
    }
  },
  mounted () {
    if (!getUserName()) {
      this.$router.push('/login')
    }
  },
  computed: {
  }
}
</script>

<style scoped>
.content-list {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: scroll;
  background-image: url(/static/images/login_bg.jpg);
  background-size: 100% 100%;
  background-position: center center;
}
.footer-nav {
    position: fixed;
    bottom: 0;
    z-index: 102;
    width: 100%;
}
</style>
