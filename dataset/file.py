class File:

    def __init__(self, filename):
        fs = filename.find('.')
        self.name = filename[:fs]
        self.extention = filename[fs+1:]

    def __repr__(self):
        _str = ''
        _str += f"{self.name}\n{self.extention}"
        return _str

