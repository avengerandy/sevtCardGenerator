<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-4 mainCol">
        <printCanvas/>
      </div>
      <div class="col-8 mainCol">
        <ul class="nav nav-tabs" id="commontTab" role="tablist">
          <li class="nav-item" @click="changeComponent('uploadPic')">
            <a class="nav-link" :class="{active: uploadPicIsActive}">角色圖</a>
          </li>
          <li class="nav-item" @click="changeComponent('monsterCard')">
            <a class="nav-link" :class="{active: monsterCardIsActive}">內容</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">資訊</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">輸出相關</a>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="#" @click="downloadCanvas" id="download">輸出</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#">dpiConverter</a>
            </div>
          </li>
        </ul>
        <keep-alive>
          <component :is="rightComponent"></component>
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<script>
import printCanvas from './components/printCanvas'
import uploadPic from './components/uploadPic'
import monsterCard from './components/monsterCard'
import eventbus from './js/eventbus.js';

import 'bootstrap'

export default {
  data() {
    return {
      rightComponent: 'uploadPic'
    }
  },
  components: {
    printCanvas,
    uploadPic,
    monsterCard
  },
  computed: {
    uploadPicIsActive: function () {
      return this.rightComponent == 'uploadPic'
    },
    monsterCardIsActive: function () {
      return this.rightComponent == 'monsterCard'
    }
  },
  methods: {
    downloadCanvas() {
      document.getElementById('printCanvas').toBlob(function(blobData){
        let downloadLink = document.createElement('a');
        downloadLink.href = window.URL.createObjectURL(blobData);
        downloadLink.download = 'card.png';
        downloadLink.click();
      });
    },
    changeComponent(componentName) {
      this.rightComponent = componentName
    }
  }
}
</script>

<style scoped lang="scss">

  $borderColor: white;
  $borderStyle: solid;
  $borderWidth: 3px;
  $fullHeight: 100%;

  .nav-item {
    cursor: pointer;
  }

  .container-fluid, .row {
    height: $fullHeight;
  }

  #commontTab {
    position:sticky; 
    top: 0px;
    z-index: 9;
    background-color: #272B30;
  }
  
  .mainCol {
    height: $fullHeight;
    border-right-color: $borderColor;
    border-right-style: $borderStyle;
    border-left-color: $borderColor;
    border-left-style: $borderStyle;
    &:nth-child(even) {
      max-height: 100%;
      overflow-y: scroll;
      border-right-width: $borderWidth;
      border-left-width: $borderWidth / 2;
    }
    &:nth-child(odd) {
      display:flex;
      align-items:center;
      border-right-width: $borderWidth / 2;
      border-left-width: $borderWidth;
    }
  }
</style>
