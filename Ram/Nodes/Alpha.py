from Ram.Nodes.Char import CharFreq


class Alphabetical(CharFreq):
    def __init__(self, char, freq):
        super().__init__(char, freq)

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.char == otherNode.char

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Freq' and 'NoneType'"
            )

        return self.char < otherNode.char

    def __gt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'>' not supported between instances of 'Freq' and 'NoneType'"
            )
        return self.char > otherNode.char

    def __str__(self):
        return "<Alphabet Object>"
