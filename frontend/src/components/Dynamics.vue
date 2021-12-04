<template>
  <div class="dynamicsBox">
    <DynamicsHead :username=this.dusername :mytime=this.mytime></DynamicsHead>
    <DynamicsContents :content=this.content></DynamicsContents>
    <DynamicsInfo :comments=this.comments></DynamicsInfo>
  </div>
</template>

<script>
import DynamicsHead from './DynamicsHead.vue'
import DynamicsContents from './DynamicsContents.vue'
import DynamicsInfo from './DynamicsInfo.vue'
export default {
  props: ['id', 'content', 'dusername', 'mytime', 'comments'],
  components: {
    DynamicsHead,
    DynamicsContents,
    DynamicsInfo
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
</style>
