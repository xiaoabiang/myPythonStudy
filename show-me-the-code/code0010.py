from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from config import DIR_PATH, FONT_PATH
import os

def getchar():
    return chr(random.randint(65,90))


# random color 1
def getColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# random color 2
def getColor2():
    return (random.randint(0, 120), random.randint(0, 120), random.randint(0, 120))


def getrandomgif():
    image = Image.new('RGB', (60*4, 60), (255, 255, 255))
    font = ImageFont.truetype(os.path.join(FONT_PATH, 'Ubuntu-B.ttf'), 36)

    draw = ImageDraw.Draw(image)

    for x in range(240):
        for y in range(60):
            draw.point((x,y), fill=getColor1())

    for i in range(4):
        draw.text((60*i + 10, 10), getchar(), font=font, fill=getColor2())

    image = image.filter(ImageFilter.BLUR)
    image.save(os.path.join(DIR_PATH, '{}.JPG'.format(random.randint(0, 100000))),'jpeg')

if __name__ == '__main__':
    getrandomgif()
