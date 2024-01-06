class SortedList:
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insertAll(self, list, ClassName):
        for i in list:
            node = ClassName(i)
            self.insert(node)
        return self

    def insert(self, newNode):
        self.length += 1
        if self.headNode == None:
            self.headNode = newNode
            return
        if newNode > self.headNode:
            self.__appendToHead(newNode)
            return
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode > rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        leftNode.nextNode = newNode

    def __str__(self):
        output = "<SortedList Object: "
        node = self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += "," + node.__str__()
            node = node.nextNode
        return output + ">"
