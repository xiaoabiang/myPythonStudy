import os
import fnmatch
from collections import Counter
import re


class GetFileInfo(object):

    """Docstring for GetFile. """

    def __init__(self):
        """TODO: to be defined1. """
        '''
        dirpath: dir path 
        opt : filter file names
        '''
        pass

    def getfiles(self, dirpath, opt=None):
        for dirpath, dirnames, filenames in os.walk(dirpath):
            for name in fnmatch.filter(filenames, opt):
                yield os.path.join(dirpath, name)

    def getfilehandle(self, filepaths):
        try:
            for filepath in filepaths:
                f = open(filepath, mode='rt', encoding='utf-8') 
                yield f
                f.close()
        except:
            pass

    def getlines(self, files):
        for line in files:
            yield from line

    def getwords(self, lines):
        for line in lines:
            if not line.startswith('#'):
                words = re.findall(r'\w+', line.strip())
                for word in words:
                    yield word



def main():
    aa = GetFileInfo()
    filepaths = aa.getfiles('/home/fanty/PycharmProjects/show-me-the-code', '*.py')
    files = aa.getfilehandle(filepaths)
    lines = aa.getlines(files)
    words = aa.getwords(lines)
    lists = []
    for x in words:
        lists.append(x)
    count = Counter(lists)
    print(count)

if __name__ == "__main__":
    main()
