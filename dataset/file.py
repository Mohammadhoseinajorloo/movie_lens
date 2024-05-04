class File:
    def __init__(self, filename):
        fs = filename.split(".")
        self.name = fs[0]
        self.extention = fs[1]

    def __repr__(self):
        _str = ''
        _str += f"{self.name}\n{self.extention}"
        return _str

file = File("links.csv")
print(file)
