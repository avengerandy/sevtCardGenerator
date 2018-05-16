<template>
<div class="container">
  <form>
    <div class="form-group row">
      <label for="titleFontSize" class="col-sm-2 col-form-label">名稱字體</label>
      <div class="col-sm-10">
        <input type="number" class="form-control" id="titleFontSize" v-model="titleFontSize">
      </div>
    </div>
    <div class="form-group row">
      <label for="title" class="col-sm-2 col-form-label">名稱</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="title" v-model="title" placeholder="名稱">
      </div>
    </div>
    <div class="form-group row">
      <label for="cardType" class="col-sm-2 col-form-label">類型</label>
      <div class="col-sm-10">
        <div class="form-check">
          <label class="form-check-label">
            <input type="radio" class="form-check-input" name="typeRadios" value="1" v-model="cardType">
            英靈卡
          </label>
        </div>
        <div class="form-check">
          <label class="form-check-label">
            <input type="radio" class="form-check-input" name="typeRadios" value="2" v-model="cardType">
            其他卡
          </label>
        </div>
      </div>
    </div>
    <div v-show="isMonster">
      <div class="form-group row">
        <label for="leftTopIcon" class="col-sm-2 col-form-label">左上物件</label>
        <div class="col-sm-10">
          <select class="form-control" v-model="leftTopIcon" id="leftTopIcon" >
            <option value="1">法書</option>
            <option value="2">地圖</option>
            <option value="3">劍</option>
            <option value="4">鐵鎚</option>
            <option value="5">徽章</option>
          </select>
        </div>
      </div>
      <div class="form-group row">
        <label for="attribute" class="col-sm-2 col-form-label">屬性珠</label>
        <div class="col-sm-10">
          <select class="form-control" v-model="attribute" id="attribute">
            <option value="mine">雷</option>
            <option value="wind">風</option>
            <option value="grass">草</option>
            <option value="water">水</option>
            <option value="fire">火</option>
          </select>
        </div>
      </div>
      <div class="form-group row">
        <label for="romanNumeral" class="col-sm-2 col-form-label">羅馬數</label>
        <div class="col-sm-10">
          <select class="form-control" v-model="romanNumeral" id="romanNumeral">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
          </select>
        </div>
      </div>
      <div class="form-group row">
        <label for="act" class="col-sm-2 col-form-label">攻擊</label>
        <div class="col-sm-4">
          <input type="number" class="form-control" v-model="act" id="act">
        </div>
        <label for="def" class="col-sm-2 col-form-label">防守</label>
        <div class="col-sm-4">
          <input type="number" class="form-control" v-model="def" id="def">
        </div>
      </div>
    </div>
    <div v-show="!isMonster">
      <div class="form-group row">
        <label for="otherLeftTopIcon" class="col-sm-2 col-form-label">卡類</label>
        <div class="col-sm-10">
          <select class="form-control" id="otherLeftTopIcon" v-model="otherLeftTopIcon">
            <option value="religion">信仰</option>
            <option value="equip">裝備</option>
            <option value="strategy">謀略</option>
            <option value="environment">環境</option>
          </select>
        </div>
      </div>
      <div class="form-group row">
        <label for="contentFirstFontSize" class="col-sm-2 col-form-label">標題字體</label>
        <div class="col-sm-10">
          <input type="number" class="form-control" id="contentFirstFontSize" v-model="contentFirstFontSize">
        </div>
      </div>
      <div class="form-group row">
        <label for="fontSize" class="col-sm-2 col-form-label">字體</label>
        <div class="col-sm-10">
          <input type="number" class="form-control" id="fontSize" v-model="contentFontSize">
        </div>
      </div>
      <div class="form-group row">
        <label for="contentTextarea" class="col-sm-12">內容</label>
        <div class="col-sm-12">
          <textarea class="form-control" id="contentTextarea" rows="5" v-model="content"></textarea>
        </div>
      </div>
    </div>
    <label class="btn btn-primary" @click="printAll">重繪</label>
  </form>
</div>
</template>

<script>
import eventbus from '../js/eventbus.js';

export default {
  data () {
    return {
      title: '',
      titleFontSize: 90,
      act: 0,
      def: 0,
      leftTopIcon: '1',
      attribute: 'mine',
      romanNumeral: '1',
      cardType: '1',
      otherLeftTopIcon: 'religion',
      content: '',
      contentFontSize: 70,
      contentFirstFontSize: 100
    }
  },
  watch: {
    title: function (title) {
      eventbus.$emit('printTitle', title);
    },
    act: function (act) {
      eventbus.$emit('printAct', act);
    },
    def: function (def) {
      eventbus.$emit('printDef', def);
    },
    leftTopIcon: function (leftTopIcon) {
      eventbus.$emit('printLeftTopIcon', leftTopIcon);
    },
    romanNumeral: function (romanNumeral) {
      eventbus.$emit('printNum', romanNumeral);
    },
    attribute: function (attribute) {
      eventbus.$emit('printAttribute', attribute);
    },
    cardType: function (cardType) {
      eventbus.$emit('printCardType', cardType);
    },
    otherLeftTopIcon: function (otherLeftTopIcon) {
      eventbus.$emit('printOtherLeftTopIcon', otherLeftTopIcon);
    },
    content: function (content) {
      eventbus.$emit('printContent', content);
    },
    contentFontSize:function (contentFontSize) {
      eventbus.$emit('printContentFontSize', contentFontSize);
    },
    contentFirstFontSize:function (contentFirstFontSize) {
      eventbus.$emit('printContentFirstFontSize', contentFirstFontSize);
    },
    titleFontSize:function (titleFontSize) {
      eventbus.$emit('printTitleFontSize', titleFontSize);
    }
  },
  computed: {
    isMonster: function () {
      return this.cardType == '1'
    }
  },
  methods: {
    printAll:function () {
      eventbus.$emit('printAll');
    }
  }
}
</script>

<style lang="scss" scoped>
  .container {
    padding-top: 5%;
    padding-bottom: 5%;
    align-items: center;
  }
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
