# sevt

> A sevt card game's card generator 

## Screenshot

image cropper made by [Cropper.js](https://fengyuanchen.github.io/cropperjs/)
<img src = "https://raw.githubusercontent.com/avengerandy/RouteMap/develop/routemap.png" width="100%"/>

you can set property and preview of card will show on left area
<img src = "https://raw.githubusercontent.com/avengerandy/RouteMap/develop/routemap.png" width="100%"/>
<img src = "https://raw.githubusercontent.com/avengerandy/RouteMap/develop/routemap.png" width="100%"/>

## dpiConverter
if you don't have Photoshop or other graphics editing program, dpiConverter is a simple python code for change images DPI, so that you can print cards in real world

create your environment use

```bash
  cd dpiConverter
  virtualenv ENV
  source ENV/Scripts/activate
  pip install -r requirements.txt
```

if you want build it to exe

```bash
  cd dpiConverter
  ./ENV/Scripts/pyinstaller.exe -F --hidden-import PIL index.py
```

## Build Setup for Sevt

``` bash
cd sevt

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
