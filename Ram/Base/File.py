from Ram.IO.File import FileHandler


class File:
    def __init__(self, filename):
        self.filename = filename
        self.fileHandle = FileHandler()
        self.txt = self.fileHandle.readFile(filename)

    def getFileName(self):
        return self.filename
