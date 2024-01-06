from Ram.Base.Node import Node


class CharFreq(Node):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        super().__init__()

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.freq == otherNode.freq

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Freq' and 'NoneType'"
            )
        if self.freq == otherNode.freq:  # if freq same sort by alpha
            return self.char > otherNode.char
        else:
            return self.freq < otherNode.freq

    def __gt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'>' not supported between instances of 'Freq' and 'NoneType'"
            )
        if self.freq == otherNode.freq:  # if freq same sort by alpha
            return self.char < otherNode.char
        else:
            return self.freq > otherNode.freq

    def __str__(self):
        s = f" {self.char}:{self.freq} "
        return s

    def getChar(self):
        return self.char

    def getFreq(self):
        return self.char
