<template>
   <div class="dynamicsContents">
     <div class="content" v-bind:class="[isOpen ? 'openHeight' : 'foldHeight']">
       《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。
       《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。
       《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。
       《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。
       《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。
     </div>
     <div @click="toggleContent" class="toggleText">
       {{ toggleText }}
     </div>
   </div>
</template>

<script type="text/ecmascript-6">
export default {
  name: 'dynamicsInfo',
  data () {
    return {
      isOpen: false,
      toggleText: '展开全文'
    }
  },
  methods: {
    toggleContent: function () {
      if (this.isOpen === false) {
        this.isOpen = true
        this.toggleText = '收起'
      } else {
        this.isOpen = false
        this.toggleText = '展开全文'
      }
    }
  }
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
      .foldHeight
        height: 110px
      .openHeight
        height: auto
      .toggleText
        color: #a70008
        cursor: pointer

</style>
