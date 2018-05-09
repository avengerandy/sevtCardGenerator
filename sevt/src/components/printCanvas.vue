<template>
  <canvas ref="printCanvas"></canvas>
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
      cardData: {
        croppedCanvas: null,
        title: '',
        titleFontSize: 90,
        act: 0,
        def: 0,
        leftTopIcon: '1',
        num: '1',
        attribute: 'mine',
        cardType: '1',
        otherLeftTopIcon: 'religion',
        content: '',
        contentFontSize: 70,
        contentFirstFontSize: 100
      }
    }
  },
  mounted () {
    this.canvas = this.$refs['printCanvas'];
    this.canvasContext = this.canvas.getContext('2d');
    this.canvas.setAttribute('height', config.cardWidthPx * config.cardRatio);
    this.canvas.setAttribute('width', config.cardWidthPx);
    this.resizeRatio();
    $(window).on("resize", function() {
      this.resizeRatio();
      this.print();
    }.bind(this));
    eventbus.$on('printBackground', this.printBackground);
    eventbus.$on('printTitle', this.printTitle);
    eventbus.$on('printAct', this.printAct);
    eventbus.$on('printDef', this.printDef);
    eventbus.$on('printLeftTopIcon', this.printLeftTopIcon);
    eventbus.$on('printNum', this.printNum);
    eventbus.$on('printAttribute', this.printAttribute);
    eventbus.$on('printCardType', this.printCardType);
    eventbus.$on('printOtherLeftTopIcon', this.printOtherLeftTopIcon);
    eventbus.$on('printContent', this.printContent);
    eventbus.$on('printContentFontSize', this.printContentFontSize);
    eventbus.$on('printContentFirstFontSize', this.printContentFirstFontSize);
    eventbus.$on('printTitleFontSize', this.printTitleFontSize);
    eventbus.$on('output', this.output);
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
    output: function() {
      this.canvas.toBlob(function(blobData) {
        let downloadLink = document.createElement('a');
        downloadLink.href = window.URL.createObjectURL(blobData);
        let title = this.cardData.title ? this.cardData.title : 'card' ;
        downloadLink.download = title + '.png';
        downloadLink.click();
      }.bind(this));
    },
    resizeRatio: function() {
      this.canvas.style.height = this.canvas.clientWidth * config.cardRatio + 'px';  
    },
    print: function() {
      this.canvasContext.drawImage(imageData.back, 0, 0, this.canvas.getAttribute('width'), this.canvas.getAttribute('height'));
      this.canvasContext.drawImage(this.cardData.croppedCanvas, 0, 0, this.canvas.getAttribute('width'), this.canvas.getAttribute('height'));
      if (this.cardData.cardType == '1') {
        this.canvasContext.drawImage(
          imageData.monster, 
          0, 0, 
          this.canvas.getAttribute('width'), 
          this.canvas.getAttribute('height')
        );
        let leftTopIconImage
        switch (this.cardData.leftTopIcon) {
          case '1':
            leftTopIconImage = imageData.leftTopIconMagicBook;
            break;
          case '2':
            leftTopIconImage = imageData.leftTopIconMap;
            break;
          case '3':
            leftTopIconImage = imageData.leftTopIconSword;
            break;
          case '4':
            leftTopIconImage = imageData.leftTopIconHammer;
            break;
          case '5':
            leftTopIconImage = imageData.leftTopIconInsignia;
            break;
        }
        this.canvasContext.drawImage(
          leftTopIconImage, 
          0, 0, 
          this.canvas.getAttribute('width'), 
          this.canvas.getAttribute('height')
        );
        let attributeImage
        switch (this.cardData.attribute) {
          case 'fire':
            attributeImage = imageData.attribute_fire;
            break;
          case 'grass':
            attributeImage = imageData.attribute_grass;
            break;
          case 'mine':
            attributeImage = imageData.attribute_mine;
            break;
          case 'water':
            attributeImage = imageData.attribute_water;
            break;
          case 'wind':
            attributeImage = imageData.attribute_wind;
            break;
        }
        this.canvasContext.drawImage(
          attributeImage, 
          0, 0, 
          this.canvas.getAttribute('width'), 
          this.canvas.getAttribute('height')
        );
        let numImage
        switch (this.cardData.num) {
          case '1':
            numImage = imageData.num_one;
            break;
          case '2':
            numImage = imageData.num_two;
            break;
          case '3':
            numImage = imageData.num_three;
            break;
          case '4':
            numImage = imageData.num_four;
            break;
          case '5':
            numImage = imageData.num_five;
            break;
          case '6':
            numImage = imageData.num_six;
            break;
        }
        this.canvasContext.drawImage(
          numImage, 
          0, 0, 
          this.canvas.getAttribute('width'), 
          this.canvas.getAttribute('height')
        );
        let fontPx = config.cardWidthPx * 0.025;
        this.canvasContext.fillStyle = "rgba(255, 255, 255, 1)";
        this.canvasContext.font = "italic " + fontPx + "px Arial, cwTeXFangSong";
        this.canvasContext.fillText(
          this.cardData.act, 
          config.cardWidthPx * (0.2 - this.cardData.act.toString().length * 0.005), 
          config.cardWidthPx * 1.202
        );
        this.canvasContext.fillText(
          this.cardData.def, 
          config.cardWidthPx * (0.77 - this.cardData.def.toString().length * 0.005), 
          config.cardWidthPx * 1.265
        );
      } else {
        let otherLeftTopIcon
        switch (this.cardData.otherLeftTopIcon) {
          case 'religion':
            otherLeftTopIcon = imageData.religion;
            break;
          case 'equip':
            otherLeftTopIcon = imageData.equip;
            break;
          case 'strategy':
            otherLeftTopIcon = imageData.strategy;
            break;
          case 'environment':
            otherLeftTopIcon = imageData.environment;
            break;
        }
        this.canvasContext.drawImage(
          otherLeftTopIcon, 
          0, 0, 
          this.canvas.getAttribute('width'), 
          this.canvas.getAttribute('height')
        );

        let contentList = this.cardData.content.split("\n");
        let lines = contentList.length;
        this.canvasContext.fillStyle = "rgba(77, 57, 0, 1)";
        this.canvasContext.font = this.cardData.contentFirstFontSize + "px Arial, cwTeXFangSong";
        if(this.cardData.otherLeftTopIcon != 'environment') {
          contentList[0] = '【' + contentList[0] + '】';
        }
        this.canvasContext.fillText(
          contentList[0], 
          config.cardWidthPx * 0.07, 
          config.cardWidthPx * 1.05 + parseInt(this.cardData.contentFirstFontSize)
        );
        
        this.canvasContext.font = this.cardData.contentFontSize + "px Arial, cwTeXFangSong";
        let lineHigh = this.cardData.contentFontSize / 2;
        if(this.cardData.otherLeftTopIcon == 'environment') {
          lineHigh = 0;
        }
        for (let index = 0; index < lines; index++) {
          if(index === 0){
            continue;
          }
          this.canvasContext.fillText(
            contentList[index], 
            config.cardWidthPx * 0.07, 
            config.cardWidthPx * 1.05 + parseInt(this.cardData.contentFirstFontSize) + this.cardData.contentFontSize * index + lineHigh
          );
        }
      }
      this.canvasContext.fillStyle = "rgba(229, 205, 197, 1)";
      //let fontPx = config.cardWidthPx * 0.05;
      this.canvasContext.font = this.cardData.titleFontSize + "px Arial, cwTeXFangSong";
      this.canvasContext.fillText(
        this.cardData.title, 
        config.cardWidthPx * 0.6, 
        config.cardWidthPx * 0.172 - (90 - parseInt(this.cardData.titleFontSize))/2.5
      );
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
    },
    printNum: function(num) {
      this.cardData.num = num;
    },
    printAttribute: function(attribute) {
      this.cardData.attribute = attribute;
    },
    printCardType: function(cardType) {
      this.cardData.cardType = cardType;
    },
    printOtherLeftTopIcon: function(otherLeftTopIcon) {
      this.cardData.otherLeftTopIcon = otherLeftTopIcon;
    },
    printContent: function(content) {
      this.cardData.content = content;
    },
    printContentFontSize: function(contentFontSize) {
      this.cardData.contentFontSize = contentFontSize;
    },
    printContentFirstFontSize: function(contentFirstFontSize) {
      this.cardData.contentFirstFontSize = contentFirstFontSize;
    },
    printTitleFontSize: function(titleFontSize) {
      this.cardData.titleFontSize = titleFontSize;
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
