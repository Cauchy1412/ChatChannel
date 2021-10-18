<template>
  <div>
    <div class="header">
      <mu-appbar title='关于'>
        <mu-icon-button icon="chevron_left" slot="left" @click="goback" />
        <mu-icon-button icon="expand_more" slot="right"/>
      </mu-appbar>
    </div>
    <div class="content">
      <mu-list>
        <mu-list-item title="三元一次方程组" describeText="组名">
          <mu-icon value="face" color="indigo" slot="left"/>
        </mu-list-item>
        <mu-list-item title="许远帆、周华盛、史默迪" describeText="组员">
          <mu-icon value="backup" color="indigo" slot="left"/>
        </mu-list-item>
        <mu-list-item title="郎波" describeText="指导老师">
          <mu-icon value="book" color="indigo" slot="left"/>
        </mu-list-item>
        <mu-list-item title="120812312@qq.com" describeText="邮箱">
          <mu-icon value="subject" color="indigo" slot="left"/>
        </mu-list-item>
      </mu-list>
    </div>
  </div>
</template>

<script>
import { getUserName } from '../../utils/localStorage'
export default{
  data () {
    return {
      username: ''
    }
  },
  mounted () {
    if (!getUserName()) {
      this.$router.push('/login')
    }
    this.username = getUserName()
  },
  methods: {
    goback () {
      this.$router.goBack()
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
  background-image: url(/static/images/about.jpg);
  background-size: 100% 100%;
  background-position: center center;
}
.mu-appbar {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 10%;
  background-color: rgba(0,0,0,.78);
}
</style>
