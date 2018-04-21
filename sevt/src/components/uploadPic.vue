<template>
  <div id="imageContenter">
    <input type="checkbox" v-model="autoCrop" id="autoCropCheckbox"/>
    <label for="autoCropCheckbox">即時裁切</label>
    <input type="file" id="change" accept="image" @change="change">
    <label for="change" class="btn btn-primary">上傳</label>
    <label class="btn btn-primary" @click="crop">切割</label>
    <br>
    <img v-show="url" id="image" :src="url" alt="Picture">
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
      autoCrop: false
    }
  },
  mounted () {
    var uploadPicVue = this;
    var image = document.getElementById('image');
    this.cropper = new Cropper(image, {
      aspectRatio: 62/90,
      viewMode: 1,
      background:false,
      zoomable:false,
      responsive:false,
      autoCropArea:1,
      ready: function () {
        uploadPicVue.croppable = true;
      },
      crop: function () {
        if(uploadPicVue.autoCrop) uploadPicVue.crop();
      },
    });
  },
  methods: {
    change (e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.url = window.URL.createObjectURL(files[0]);  
      this.cropper.replace(this.url);
    },
    crop () {
      var croppedCanvas;
      if (!this.croppable) {
        return;
      }
      croppedCanvas = this.cropper.getCroppedCanvas();
      eventbus.$emit('printBackground', croppedCanvas);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .btn:focus,.btn:active {
    outline: none;
    box-shadow: none;
  }
  #change {
    display:none;
  }
  #image {
    width: 100%;
    max-width: 100%;
  }
  input[type="checkbox"] {
    display:none;
    + label {
      transition: all .3s ease;
      background-color: #ccc;
      color: #000;
      border-radius: 10px;
      cursor: pointer;
      user-select: none;
      margin: 0 10px;
      padding: 5px;
    }
    &:checked + label {
      background-color: #000;
      color: #fff;
    }
  }
</style>
