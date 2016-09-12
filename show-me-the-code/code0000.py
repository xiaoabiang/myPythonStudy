from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os 
from config import DIR_PATH, FONT_PATH
import random

def test():
    try:
        img = Image.open(os.path.join(DIR_PATH,'test.png'))
        s =  input("Please input the number to display:")
        try:
            num = 0 if s == '' else int(s)
            image_width = img.size[0]
            image_height = img.size[1]
    
            font_size = 60*image_height//480
            font_height = 60
            font_width = 40
            text_x = image_width - font_width * len(str(num))
            text_y = 5
    
            font = ImageFont.truetype(os.path.join(FONT_PATH, 'Ubuntu-B.ttf'),
                                      60)
    
            draw = ImageDraw.Draw(img)
            draw.text((text_x, text_y), str(num), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), font=font)
    
            img.save(os.path.join(DIR_PATH, 'new_image.png'))
        except Exception as ex:
            print(ex)
    except:
        print('Can\'t find specified file')


if __name__ == '__main__':
    test()


