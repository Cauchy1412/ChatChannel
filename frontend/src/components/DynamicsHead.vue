<template>
  <div class="dynamicsHead">
      <div class="avatar">
        <img src="..\..\static\images\avatar1.jpg" alt="">
      </div>
      <div class="userText">
        <span class="userName">{{ this.userName }}</span>
        <span class="time">{{ this.getdate }}</span>
      </div>
  </div>
</template>
<style>

</style>
<script type="text/ecmascript-6">
import dateFormat from '../utils/date'
export default {
  props: ['username', 'mytime'],
  computed: {
    getdate () {
      return dateFormat(new Date(this.mytime), 'yyyy-MM-dd HH:mm:ss')
    }
  }
}

</script>

<style lang="stylus">
  @import "../assets/style/mixins.styl"
  .dynamicsHead
    width:100%
    height:50px
    line-height:50px
    .avatar
      width: 40px
      height: 50px;
      line-height: 50px
      border-radius:(50%)
      padding: 5px 0
      float: left
      margin-right:12px
      &>img
        width: 40px
        height: 40px
    .userText
      height:50px;
      float:left
      .userName,.time
         display: block
         width: 100%
         height: 25px
         line-height: 25px
      .userName
        color:#333
      .time
        color:#999
    .headButton
      height: 50px
      line-height: 50px
      float:right
      .oneButton
        display: inline-block
        cursor: pointer
        &:hover
          color:#BA0101
          &>.icon
            color:#BA0101
      .oneButton:first-child
        margin-right:32px;
</style>
