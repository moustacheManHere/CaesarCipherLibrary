from Ram.Base.Node import Node


class LetterNode(Node):
    def __init__(self, char, id):
        super().__init__()
        if isinstance(char, str):
            self.char = char[0].lower()
        else:
            raise TypeError
        self.id = id  # to differentiate A and A when both in nodes

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.id == otherNode.id

    def __str__(self):
        s = f" {self.char}:{self.id} "
        return s

    def getChar(self):
        return self.char
