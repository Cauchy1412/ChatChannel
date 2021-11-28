<template>
   <div class="dynamicsInfo">
      <div class="phone">
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-shouji"></use>
        </svg>
        来自<span class="phoneNumber">{{ phoneNumber }}</span>
      </div>
      <div class="otherInfo">
        <div class="read">浏览<span>72次</span></div>
        <div class="iconBox">
          <div @click="collect">
            <svg :class="['icon',{iconActive:isCollect}]" aria-hidden="true">
              <use xlink:href="#icon-icon1"></use>
            </svg>
            收藏
          </div>
          <div @click="like">
            <svg :class="['icon',{iconActive:isLike}]" aria-hidden="true">
              <use xlink:href="#icon-dianzan"></use>
            </svg>
            点赞
          </div>
          <div @click="comment">
            <svg class="icon" aria-hidden="true">
              <use xlink:href="#icon-anzhuo34"></use>
            </svg>
            评论
          </div>
          <div>
            <svg class="icon" aria-hidden="true">
              <use xlink:href="#icon-iconfontforward"></use>
            </svg>
            转发
          </div>
        </div>
      </div>
      <div class="likeList">
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-dianzan"></use>
        </svg>
        <div class="userList"></div>
      </div>
      <textarea :class="['commentBox',{commentBoxHeight:isFocus}]" id="commentBox" @click="comment">评论</textarea>
   </div>
</template>

<script type="text/ecmascript-6">
export default {
  name: 'dynamicsInfo',
  data () {
    return {
      phoneNumber: 'iphone 7 plus',
      isCollect: false,
      isLike: false,
      isComment: false,
      isFocus: false,
      commentContent: '评论'
    }
  },
  methods: {
    collect: function () {
      if (this.isCollect === false) {
        this.isCollect = true
      } else {
        this.isCollect = false
      }
    },
    like: function () {
      if (this.isLike === false) {
        this.isLike = true
      } else {
        this.isLike = false
      }
    },
    comment: function () {
      this.isFocus = true
      document.getElementById('commentBox').focus()
      this.commentContent = ''
    }
  }
}
</script>

<style lang="stylus">
  .dynamicsInfo
    width:100%
    .phone
      width:100%
      height:30px
      line-height:30px
      color:#999
    .otherInfo
      height: 40px
      padding-bottom: 15px
      color:#999
      line-height: 40px;
      border-bottom: 1px solid #E7E7E7;
      .read
        float:left
        display:inline-block
      .iconBox
        float:right
        &>div
          display:inline-block
          float:left
          margin-right: 30px
          color:#333
          cursor:pointer
          &:hover
            color:#BA0101
            &>.icon
              color:#BA0101
        &>div:last-child
          margin-right: 15px
          &>div>span
            color:#999
    .likeList
      width:100%
      height:auto
      overflow:hidden
      word-wrap: break-word
      word-break: break-all
      padding:10px 0
      cursor:pointer
    .commentBox
      width:100%
      height:40px;
      line-height:16px;
      border:1px solid #E7E7E7
      margin-bottom:5px
      padding:13px
      resize: none;
      overflow-y:auto
    ::-webkit-scrollbar
      width:2px;
      height:2px
    ::-webkit-scrollbar-thumb
      background-color:#c2c2c2;
      background-clip:padding-box;
      min-height:18px
    ::-webkit-scrollbar-thumb:hover
      background-color:#A0A0A0
    .commentBoxHeight
      height:74px
</style>
