<template>
  <div>
    <input type="checkbox" v-model="autoCrop" id="autoCropCheckbox"/>
    <label for="autoCropCheckbox">即時裁切</label>
    <label class="btn btn-primary">
      <input type="file" accept="image" @change="change">
      上傳
    </label>
    <label class="btn btn-primary" @click="crop">切割</label>
    <br>
    <img v-show="url" ref="mainImage" :src="url" alt="Picture">
  </div>
</template>

<script>
import '../../node_modules/cropperjs/dist/cropper.min.css';
import Cropper from 'cropperjs';
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
    this.cropper = new Cropper(this.$refs['mainImage'], {
      aspectRatio: 62/90,
      viewMode: 1,
      background:false,
      zoomable:false,
      responsive:false,
      autoCropArea:1,
      ready: function () {
        this.croppable = true;
      }.bind(this),
      crop: function () {
        if(this.autoCrop) this.crop();
      }.bind(this),
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
      if (!this.croppable) {
        return;
      }
      eventbus.$emit('printBackground', this.cropper.getCroppedCanvas());
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
  input[type="file"] {
    display:none;
  }
  img {
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
