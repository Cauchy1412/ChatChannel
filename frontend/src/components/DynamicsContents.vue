<template>
   <div class="dynamicsContents">
     <div class="content" v-bind:class="Height">
       {{ this.content }}
     </div>
   </div>
</template>

<script type="text/ecmascript-6">
export default {
  name: 'dynamicsInfo',
  props: ['content']
}
</script>

<style lang="stylus">
  .dynamicsContents
      width: 100%
      height: auto
      padding: 25px 0
      .content
        line-height: 22px;
        overflow-y: hidden
      .Height
        height: auto


</style>
