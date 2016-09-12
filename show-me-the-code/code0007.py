from code0004 import GetFileInfo


class GetCodeNumber(GetFileInfo):
    def __init__(self):
        super(GetCodeNumber, self).__init__()

    def getwords(self, lines):
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                yield ('#', 1)
            elif line == '':
                yield ('space', 1)
            else:
                yield ('coding', 1)

    def getnumbers(self, dirpath, opt):
        filepaths = self.getfiles(dirpath, opt)
        files = self.getfilehandle(filepaths)
        lines = self.getlines(files)
        words = aa.getwords(lines)
        dicts = dict()
        for x in words:
            dicts[x[0]] = dicts.get(x[0], 0) + 1
        return dicts


if __name__ == "__main__":
    aa = GetCodeNumber()
    dicts = aa.getnumbers('/home/fanty/PycharmProjects', '*.py')
    print(dicts)
