<template>
<div id="demo">
    <div>  
      <img id="image" :src="url" alt="Picture">
    </div>
    <button type="button" id="button" @click="crop">确定</button>
    <canvas id="Dcanvas" width="620" height="900"></canvas>
    <div style="padding:20px;">
        <div style="margin-top:20px;">
          <input type="file" id="change" accept="image" @change="change">  
          <label for="change"></label>
        </div>
    </div>
  </div>
</template>

<script>
import '../../node_modules/cropperjs/dist/cropper.min.css'
import Cropper from 'cropperjs'  
import eventbus from '../js/eventbus.js';

export default {
  data () {
    return {
      cropper:'',
      croppable: false,
      url:'',
      autoCrop: true
    }
  },
  mounted () {
    var self = this;
    var image = document.getElementById('image');
    this.cropper = new Cropper(image, {
      aspectRatio: 62/90,
      viewMode: 1,
      background:false,
      zoomable:false,
      ready: function () {
        self.croppable = true;
      },
      crop: function () {
        if(self.autoCrop) self.crop();
      },
    });
  },
  methods: {
    change (e){
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.url = window.URL.createObjectURL(files[0]); 
      if(this.cropper){  
        this.cropper.replace(this.url);  
      }
    },
    crop (){ 
      var croppedCanvas;
      if (!this.croppable) {
        return;
      }
      croppedCanvas = this.cropper.getCroppedCanvas();
      /*var c=document.getElementById("Dcanvas");
      var ctx=c.getContext("2d");
      ctx.drawImage(croppedCanvas, 0, 0, 620, 900);*/
      eventbus.$emit('printBackground', croppedCanvas);
    },
  }
}  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#Dcanvas {
  max-width: 100%;
}
#demo .show {
  max-width: 100%;
}  
#demo .picture {  
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
}
#demo .container {
    z-index: 99;
    position: fixed;
    padding-top: 60px;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    background:rgba(0,0,0,1);
}
#demo #image {
  max-width: 100%;  
}
</style>
