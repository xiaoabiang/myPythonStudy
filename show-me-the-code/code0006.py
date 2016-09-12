import os
from config import DIR_PATH
from code0004 import GetFileInfo
from collections import Counter


class GetCodeNumber(GetFileInfo):
    def __init__(self):
        super(GetCodeNumber, self).__init__()

    def getwords(self, lines):
        for line in lines:
            words = line.split()
            for word in words:
                yield word

    def getnumbers(self, dirpath, opt):
        filepaths = self.getfiles(dirpath, opt)
        files = self.getfilehandle(filepaths)
        lines = self.getlines(files)
        words = self.getwords(lines)
        lists = []
        for x in words:
            lists.append(x)
        return lists


def openfile():
    filenamelist = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(DIR_PATH,
                                                             'texts')):
        for value in filenames:
            filenamelist.append(os.path.join(dirpath, value))
    for filename in filenamelist:
        with open(filename, 'rb') as f:
            for line in f.readlines():
                try:
                    print(line.decode('utf-8'))
                except Exception as ex:
                    print(ex)


def main():
    aa = GetCodeNumber()
    lists = aa.getnumbers(os.path.join(DIR_PATH, 'texts'), '*.txt')
    mm = Counter(lists)
    print(mm)


if __name__ == "__main__":
    main()
