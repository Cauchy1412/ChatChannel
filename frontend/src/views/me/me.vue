<template>
  <div>
    <div class="header">
      <mu-appbar :title='username'>
        <mu-icon-button icon="chevron_left" slot="left" @click="goback" />
        <mu-icon-button icon="expand_more" slot="right"/>
      </mu-appbar>
    </div>
    <div class="content">
      <mu-list>
        <mu-list-item title="个人中心">
          <mu-icon slot="left" value="inbox"/>
        </mu-list-item>
        <mu-list-item title="我的好友">
          <mu-icon slot="left" value="grade"/>
        </mu-list-item>
        <mu-list-item title="我的动态">
          <mu-icon slot="left" value="send"/>
        </mu-list-item>
        <mu-list-item title="新密码">
          <mu-icon slot="left" value="drafts"/>
          <mu-text-field label="密码" type="password" labelFloat name="password" v-model="password" />
        </mu-list-item>
        <mu-list-item title="更新密码" @click="updatepassword">
          <mu-icon slot="left" value="send"/>
        </mu-list-item>
        <mu-list-item title="反馈">
          <mu-icon slot="left" value="drafts"/>
          <mu-text-field label="反馈" type="content" labelFloat name="content" v-model="content" />
        </mu-list-item>
        <mu-list-item title="发送反馈" @click="sendcontent">
          <mu-icon slot="left" value="send"/>
        </mu-list-item>
      </mu-list>
    </div>
    <div class="logout">
      <mu-raised-button @click="logout" label="退出" backgroundColor='grey900' fullWidth/>
    </div>
  </div>
</template>

<script>
import {getUserName, removeUserName} from '../../utils/localStorage'
import { updatepassword, sendcontent } from '@/api/update'
export default{
  data () {
    return {
      username: '',
      password: '',
      content: ''
    }
  },
  mounted () {
    if (!getUserName()) {
      this.$router.push('/login')
    }
    this.username = getUserName()
  },
  methods: {
    logout () {
      removeUserName()
      this.$router.push('/login')
    },
    goback () {
      this.$router.goBack()
    },
    updatepassword () {
      return new Promise((resolve, reject) => {
        updatepassword(this.username, this.password).then(response => {
          alert('密码更新成功！')
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    sendcontent () {
      const now = new Date()
      return new Promise((resolve, reject) => {
        sendcontent(this.username, this.content, now.toISOString()).then(response => {
          alert('建议反馈成功！')
          this.content = ''
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}
</script>

<style scoped>
.content {
  position: absolute;
  left: 0;
  right: 0;
  top: 10%;
  bottom: 0;
  background-image: url(/static/images/me.jpg);
  background-size: 100% 100%;
  background-position: center center;
}
.logout {
  position: absolute;
  left: 10%;
  right: 10%;
  top: 80%;
}
.mu-appbar {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 10%;
  text-align: center;
  background-color: rgba(0,0,0,.78);
}
</style>
