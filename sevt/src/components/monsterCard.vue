<template>
<div id="demo">
    <div>  
      <img id="image" :src="url" alt="Picture">
    </div>
    <button type="button" id="button" @click="crop">确定</button>
    <canvas id="Dcanvas" width="620" height="900"></canvas>
    <div style="padding:20px;">
        <div style="margin-top:20px;">
          <input type="file" id="change" accept="image">  
          <label for="change"></label>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  mounted () {
  },
  methods: {}
}
</script>

<style scoped>
</style>
