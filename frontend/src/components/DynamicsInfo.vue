<template>
<div class="dynamicsInfo">
  <div class="comment-wrap">
    <div class="comments-list">
      <div class="comments-list-item" v-for="(item,index) in this.comments" v-bind:key="index">
        <div class="comments-list-item-heading">
          <img src="../../static/images/avatar1.jpg" />
          <span class="comments-list-item-username">{{ item.username }}</span>
        </div>
        <div class="comments-list-item-content" v-html="item.content"></div>
      </div>
      <div class="comments-list-item" v-for="(item,index) in this.commentss" v-bind:key="index">
        <div class="comments-list-item-heading">
          <img src="../../static/images/avatar1.jpg" />
          <span class="comments-list-item-username">{{ name }}</span>
        </div>
        <div class="comments-list-item-content" v-html="item"></div>
      </div>
    </div>
    <textarea class="comment-input" placeholder="请输入内容" id="textpanel" v-model="content"></textarea>
    <div class="opration">
      <div @click="saveComment" class="comment-send-btn comment-send-btn-bounce">发表评论</div>
    </div>
  </div>
  </div>
</template>

<script type="text/ecmascript-6">
import { getUserName } from '@/utils/localStorage'
export default {
  props: ['comments', 'id'],
  data () {
    return {
      name: '',
      isCollect: false,
      isLike: false,
      isComment: false,
      isFocus: false,
      flag: false,
      content: '',
      commentss: []
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
  methods: {
    saveComment () {
      this.commentss.push(this.content)
      const now = new Date()
      const commentData = {
        'user_name': this.name,
        'dynamic_id': this.id,
        'content': this.content,
        'gen_time': now.toISOString()
      }
      this.$store.dispatch('AddCommentHistory', commentData)
      this.getSocket.send(JSON.stringify(commentData))
      this.content = ''
    }
  }
}

</script>

<style lang="stylus">
  .dynamicsInfo
    width:100%

.comment-wrap {
  width: 522px;
  margin-bottom: 10px;
  .comments-list {
    background-color: #EDEDED;
    margin-top: 20px;
    .comments-list-item {
      margin-bottom: 20px;
      .comments-list-item-heading {
        display: inline-block;
        img {
          height: 32px;
          width: 32px;
          border-radius: 50%;
          vertical-align: middle;
        }
        .comments-list-item-username {
          margin-left: 5px;
          font-weight: lighter;
        }
      }
      .comments-list-item-content {
        margin: 10px 0px;
        border-bottom: 1px solid #cccccc;
        &:last-child {
          border-bottom: 0;
        }
        span {
          vertical-align: top;
        }
      }
    }
  }
  .comment-input {
    height: 100px;
    width: 500px;
    border: 1px solid #cccccc;
    border-radius: 5px;
    padding: 10px;
    resize: none;
    &:focus {
      outline: none;
    }
  }
  .opration {
    width: 522px;
    display: flex;
    justify-content: space-between;
    position: relative;
    .comment-send-btn {
      width: 80px;
      height: 30px;
      line-height: 30px;
      text-align: center;
      border: 1px solid #1da1f2;
      border-radius: 100px;
      box-sizing: border-box;
      font-weight: bold;
      font-size: 13px;
      color: #ffffff;
      background-color: #4ab3f4;
      &:hover {
        cursor: pointer;
      }
    }
    .comment-send-btn-bounce {
      position: relative;
    }
    .comment-send-btn-bounce:focus {
      outline: none;
    }
    .comment-send-btn-bounce:after {
      content: "";
      display: block;
      position: absolute;
      top: 0px;
      left: 0px;
      right: 0px;
      bottom: 0px;
      border-radius: 100px;
      border: 0px solid #1da1f2;
      opacity: 0.7;
      transition: all 0.1s;
    }
    .comment-send-btn-bounce:active:after {
      //.bounce active时 伪元素:after的样式
      opacity: 1;
      top: -5px;
      left: -5px;
      right: -5px;
      bottom: -5px;
      border-radius: 100px;
      border: 2px solid #1da1f2;
      transition: all 0.2s;
    }
  }
}
</style>
