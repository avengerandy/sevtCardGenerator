from PIL import Image
from functional import seq
from os import listdir
from os.path import isfile

images = seq(
    listdir('./images')
).filter(
    lambda x: isfile('./images/' + x)
).filter(
    lambda x: x[-4:] in ['.png', '.PNG', '.jpg', '.JPG', '.bmp', '.BMP']
).to_list()

for image in images:
    Image.open('./images/' + image).save("./output/" + image, dpi=(300,300))