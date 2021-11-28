<template>
  <div class="dynamicsHead">
      <div class="avatar">
        <img src="../assets/images/avatar.png" alt="">
      </div>
      <div class="userText">
        <span class="userName">张花花</span>
        <span class="time">4月22日 21:00</span>
      </div>
      <div class="headButton">
          <div class="oneButton">
            <svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-zhiding"></use>
          </svg>
            置顶
          </div>
          <div class="oneButton">
            <svg class="icon" aria-hidden="true">
              <use xlink:href="#icon-shanchu"></use>
            </svg>
            删除
          </div>
      </div>
  </div>
</template>
<style>

</style>
<script type="text/ecmascript-6">
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
