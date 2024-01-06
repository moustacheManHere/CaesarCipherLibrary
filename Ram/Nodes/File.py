from Ram.Files.Caesar import CaeserFile
from Ram.Base.Node import Node


class CaesarFileNode(CaeserFile, Node):
    def __init__(self, filename, ref):
        Node.__init__(self)
        CaeserFile.__init__(self, filename)
        self.breakCaesar(ref)

    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.key == otherNode.key

    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'<' not supported between instances of 'Freq' and 'NoneType'"
            )
        return self.key > otherNode.key

    def __gt__(self, otherNode):
        if otherNode == None:
            raise TypeError(
                "'>' not supported between instances of 'Freq' and 'NoneType'"
            )
        return self.key < otherNode.key  # reverse this logic so it sorts in ascending

    def __str__(self):
        s = f"CipherFile Object: Name=>{self.txt[:5]} Key=>{self.key} "
        return s
