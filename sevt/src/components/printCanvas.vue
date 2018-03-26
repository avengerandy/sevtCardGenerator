<template>
  <canvas id="printCanvas"></canvas>
</template>

<script>
import $ from 'jquery'
import eventbus from '../js/eventbus.js';
import config from '../js/config.js';
import imageData from '../js/image.js';

export default {
  data () {
    return {
      canvas: '',
      canvasContext: '',
      imageData: imageData,
      cardData: {
        croppedCanvas: null,
        title: '',
        act: 0,
        def: 0,
        leftTopIcon: 'magicBook'
      }
    }
  },
  mounted () {
    var printCanvasVue = this
    this.canvas = $("#printCanvas");
    this.canvasContext = this.canvas[0].getContext('2d');
    this.resizeRatio();
    $(window).on("resize", function() {
      printCanvasVue.resizeRatio();
      printCanvasVue.print();
    });
    eventbus.$on('printBackground', this.printBackground);
    eventbus.$on('printTitle', this.printTitle);
    eventbus.$on('printAct', this.printAct);
    eventbus.$on('printDef', this.printDef);
    eventbus.$on('printLeftTopIcon', this.printLeftTopIcon);
  },
  watch: {
    cardData: {
      deep: true,
      handler: function() {
        this.print();
      }
    }
  },
  methods: {
    resizeRatio: function() {
      this.canvas.height(
        this.canvas.width() * config.cardRatio
      );
      let Ratio = config.cardWidthPx / this.canvas.width();
      this.canvas.attr('height', this.canvas.height() * Ratio)
      this.canvas.attr('width', this.canvas.width() * Ratio)
    },
    print: function() {
      this.canvasContext.drawImage(
        this.cardData.croppedCanvas, 
        0, 
        0, 
        this.canvas.attr('width'), 
        this.canvas.attr('height')
      );
      this.canvasContext.drawImage(
        this.imageData.monster, 
        0, 
        0, 
        this.canvas.attr('width'), 
        this.canvas.attr('height')
      );
      this.canvasContext.drawImage(
        this.imageData.leftTopIcon, 
        0, 
        0, 
        this.canvas.attr('width'), 
        this.canvas.attr('height')
      );
      this.canvasContext.fillStyle = "rgba(229, 205, 197, 1)";
      let fontPx = config.cardWidthPx * 0.05;
      this.canvasContext.font = fontPx + "px Arial, cwTeXFangSong";
      this.canvasContext.fillText(this.cardData.title, config.cardWidthPx * 0.6, config.cardWidthPx * 0.172);
      fontPx = config.cardWidthPx * 0.03;
      this.canvasContext.fillStyle = "rgba(255, 255, 255, 1)";
      this.canvasContext.font = fontPx + "px Arial, cwTeXFangSong";
      this.canvasContext.fillText(this.cardData.act, config.cardWidthPx * 0.2, config.cardWidthPx * 1.202);
      this.canvasContext.fillText(this.cardData.def, config.cardWidthPx * 0.71, config.cardWidthPx * 1.26);
    },
    printBackground: function(croppedCanvas) {
      this.cardData.croppedCanvas = croppedCanvas;
    },
    printTitle: function(title) {
      this.cardData.title = title;
    },
    printLeftTopIcon: function(leftTopIcon) {
      this.cardData.leftTopIcon = leftTopIcon;
    },
    printAct: function(act) {
      this.cardData.act = act;
    },
    printDef: function(def) {
      this.cardData.def = def;
    }
  }
}
</script>

<style scoped>
  canvas {
    border: solid 1px blue;  
    width: 100%;
  }
</style>
