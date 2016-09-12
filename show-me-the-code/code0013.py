import requests
import re
from bs4 import BeautifulSoup
import lxml
import os


IMG_PATH = '/home/fanty/PycharmProjects/show-me-the-code/imgs'

def get_value(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')
    for value in soup.find_all('img'):
        yield value['src']
    # print(soup.find_all('img'))


def get_img(img_path, number):
    result = requests.get(img_path)
    with open(os.path.join(IMG_PATH,'{}.JPG'.format(number)), 'wb') as f:
        f.write(result.content)


def main():
    if not os.path.exists(IMG_PATH):
        os.mkdir(IMG_PATH)
    imgpaths = get_value('http://tieba.baidu.com/p/2166231880')
    i = 0
    for value in imgpaths:
        get_img(value, i)
        i += 1


if __name__ == "__main__":
    main()
