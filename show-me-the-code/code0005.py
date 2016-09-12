from PIL import Image
import os
from config import DIR_PATH

def filepath():
    for dirpath, dirnames, filename in os.walk(os.path.join(DIR_PATH, 'imgs')):
        for name in filename:
            if name.endswith('.JPG'):
                yield os.path.join(dirpath, name)


def getimg(filepaths):
    for filename in filepaths:
        image = Image.open(filename)
        yield image 
#
# def saveimg(images):
#     for image in images:
#         image.thumbnail(80, 80)
#         image.save()

def main():
    filepaths = filepath()
    images = getimg(filepaths)
    # saveimg(images)
    for value in images:
        print(value.filename, value.size[0], value.size[1])
        value.thumbnail((80, 80))
        value.save(value.filename)

if __name__ == "__main__":
    main()
