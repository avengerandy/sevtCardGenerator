<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-4 mainCol">
        <printCanvas/>
      </div>
      <div class="col-8 mainCol">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active">角色圖</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">內容</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">資訊</a>
          </li>
        </ul>
        <uploadPic/>
      </div>
    </div>
  </div>
</template>

<script>
import printCanvas from './components/printCanvas'
import uploadPic from './components/uploadPic'
import 'bootstrap'

export default {
  name: 'App',
  
  components: {
    printCanvas,
    uploadPic
  },
  mounted () {
  }
}
</script>

<style scoped lang="scss">
  $borderColor: white;
  $borderStyle: solid;
  $borderWidth: 3px;
  $fullHeight: 100%;

  .container-fluid, .row {
    height: $fullHeight;
  }
  
  .mainCol {
    height: $fullHeight;
    border-right-color: $borderColor;
    border-right-style: $borderStyle;
    border-left-color: $borderColor;
    border-left-style: $borderStyle;
    &:nth-child(even) {
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
