<template>
  <canvas id="printCanvas"></canvas>
</template>

<script>
import $ from 'jquery'
import eventbus from '../js/eventbus.js';

export default {
  data () {
    return {
      canvas: '',
      canvasContext: ''
    }
  },
  mounted () {
    var printCanvasVue = this
    this.canvas = $("#printCanvas");
    this.canvasContext = this.canvas[0].getContext('2d');
    this.resizeRatio();
    $(window).on("resize", function(){
      printCanvasVue.resizeRatio();
    });
    eventbus.$on('printBackground', this.printBackground);
  },
  methods: {
    resizeRatio: function(){
      this.canvas.height(
        this.canvas.width() * 90 / 62
      );
      let Ratio = 1800 / this.canvas.width();
      this.canvas.attr('height', this.canvas.height() * Ratio)
      this.canvas.attr('width', this.canvas.width() * Ratio)
    },
    printBackground: function(croppedCanvas){
      this.canvasContext.drawImage(
        croppedCanvas, 
        0, 
        0, 
        this.canvas.attr('width'), 
        this.canvas.attr('height')
      );
    },
  }
}
</script>

<style scoped>
  canvas {
    border: solid 1px blue;  
    width: 100%;
  }
</style>
