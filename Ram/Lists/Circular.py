from Ram.Base.Node import Node


class CircularLL:
    def __init__(self):
        self.headNode = None
        self.lastNode = None
        self.length = 0

    def insert(self, newNode):
        if issubclass(type(newNode), Node):
            self.length += 1
            if self.headNode == None:
                self.headNode = newNode
                self.lastNode = newNode
                return

            self.lastNode.nextNode = newNode
            self.lastNode = newNode
            self.lastNode.nextNode = self.headNode

    def getLen(self):
        return self.length

    def insertAll(self, array, NodeObj):
        for i in range(len(array)):
            node = NodeObj(array[i], i)
            self.insert(node)

    def __str__(self):
        output = "<CircularLinkedList Object: "
        node = self.headNode
        if node == None:
            return output + "<Empty List>"
        output = node.__str__()

        while node != self.lastNode:
            node = node.nextNode
            output += "," + node.__str__()
        return output + ">"
