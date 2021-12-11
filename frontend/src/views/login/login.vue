<template>
  <div class="login">
    <div class="login-header">
      <mu-appbar title="Title">
        <mu-flat-button label="Django Vue Chat" slot="default"/>
      </mu-appbar>
    </div>
    <div class="content">
      <form :model="loginForm" name="loginForm">
        <mu-text-field label="帐号" labelFloat name="username" v-model="loginForm.username" />
        <br/>
        <mu-text-field label="密码" type="password" labelFloat name="password" v-model="loginForm.password" />
        <br/>
        <mu-raised-button label="登录" @click="handleLogin" backgroundColor='grey900' fullWidth />
        <br/>
        <mu-raised-button label="注册" @click="handleRegister" backgroundColor='grey900' fullWidth />
      </form>
    </div>
  </div>
</template>

<script>
export default{
  data () {
    return {
      loading: '',
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    handleLogin () {
      if (this.loginForm.username !== '') {
        this.$store
          .dispatch('LoginByUsername', this.loginForm)
          .then(() => {
            this.password = ''
            this.$router.push({ path: '/' })
          })
          .catch(() => {
            this.password = ''
            console.log('登录失败，请检查用户名或密码！')
            alert('登录失败，请检查用户名或密码！')
          })
      } else {
        console.log('请输入用户名和密码')
      }
    },
    handleRegister () {
      if (this.loginForm.username !== '') {
        this.$store
          .dispatch('RegisterByUsername', this.loginForm)
          .then(() => {
            this.password = ''
            this.$router.push({ path: '/' })
          })
          .catch(() => {
            this.password = ''
            console.log('注册失败，请检查用户名或密码！')
            alert('您的用户名已被使用！')
          })
      } else {
        this.password = ''
        console.log('请输入用户名和密码随意')
        alert('请输入用户名和密码')
      }
    }
  },
  mounted () {
  },
  computed: {
  }
}
</script>

<style scoped>
.login {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-image: url(/static/images/login_bg.jpg);
  background-size: 100% 100%;
  background-position: center center;
}
.login-header {
    text-align: center;
    background-color: rgba(0,0,0,.78);
}
.mu-flat-button-label {
  font-size: 20px;
}
.content {
  width: 80%;
  margin: 70px auto 20px;
}
.mu-text-field {
  width: 100%;
}
.mu-text-field.has-label .mu-text-field-label.float {
  color: #121315;
}
.mu-raised-button {
  margin-top: 20px;
}
</style>
