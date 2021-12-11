<template>
  <div class="dynamicsBox">
    <textarea class="comment-input" placeholder="请输入内容" id="textpanel" v-model="input"></textarea>
    <div class="opration">
      <div @click="adddynamic" class="comment-send-btn comment-send-btn-bounce">发布动态</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['username'],
  data () {
    return {
      name: '',
      input: ''
    }
  },
  methods: {
    sleep (time) {
      return new Promise((resolve) => setTimeout(resolve, time))
    },
    adddynamic () {
      const now = new Date()
      const Data = {
        'user_name': this.username,
        'content': this.input,
        'gen_time': now.toISOString()
      }
      this.$store.dispatch('Adddynamic', Data)
      this.input = ''
      this.sleep(10).then(() => {
        this.$router.go(0)
      })
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="stylus">
  *{box-sizing:border-box}
  body
    background-color:#f9f9f9
    font-size: 14px
  .icon
    width: 1em; height: 1em
    vertical-align: -0.15em
    fill: currentColor
    overflow: hidden
    color:#999
  .iconActive
    color:#BA0101
  $width-63 = 63%
  $width-70 = 70%
  $box-shadow = 1px 1px 7px 1px rgba(0,0,0,0.3),-1px -1px 7px 1px rgba(0,0,0,0.3)

  .dynamicsBox
    @media screen and (max-width: 1366px)
      width:$width-70
    @media screen and (max-width: 1920px)
      width:$width-63
    height: auto
    margin: 0 auto
    box-shadow: $box-shadow
    margin-bottom:20px
    display:flex
    flex-flow: column nowrap
    justify-content: flex-start
    padding: 30px 40px
    overflow: hidden
    backgound-color:#fff

  .comment-input {
    height: px;
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
      margin-top:5px
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
      background-color: #123456;
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

</style>
