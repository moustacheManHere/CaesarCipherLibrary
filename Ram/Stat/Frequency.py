from Ram.Lists.Sorted import SortedList
from Ram.Nodes.Char import CharFreq
from Ram.Nodes.Alpha import Alphabetical
from Ram.Base.File import File


class Frequency(File):
    def __init__(self, filename, letter=[], freqs=[], freqFile=False):  # polymorphism

        if freqFile == True and filename is not None:
            File.__init__(self, filename)
            letterArr, freqsArr = self.fileHandle.readFreqFile(filename)
        elif filename is not None:
            File.__init__(self, filename)
            letterArr, freqsArr = self.fileHandle.readTextFrequency(filename)
        else:
            letterArr = letter
            freqsArr = freqs

        self.list = SortedList()
        self.alphaList = SortedList()

        self.insertAll(letterArr, freqsArr)

    def insertAll(self, letters, freq):
        if len(letters) != len(freq):
            print("Error: Letters and Frequency does not match!")
        for i, v in enumerate(letters):
            node = CharFreq(v, freq[i])
            alphaNode = Alphabetical(v, freq[i])
            self.list.insert(node)
            self.alphaList.insert(alphaNode)

    def getTopLetters(self, toround=False, todict=False, top=5):
        if not top > 0 or not isinstance(top, int):
            print("Error: Invalid value of top letters requested!")
            return None
        topLetter = []
        topFreq = []
        current = self.list.headNode
        for _ in range(top):
            if current == None:
                break
            topLetter.append(current.char)
            topFreq.append(current.freq)
            current = current.nextNode
        if toround:
            topFreq = [round(i, toround) for i in topFreq]
        if todict:
            pairs = zip(topLetter, topFreq)
            return dict(pairs)
        return topLetter, topFreq

    def getAlphaList(self, toround=False, todict=False):
        letters = []
        freq = []
        current = self.alphaList.headNode
        while current != None:
            letters.insert(0, current.char)
            freq.insert(0, current.freq)
            current = current.nextNode
        if toround:
            freq = [round(i, toround) for i in freq]
        if todict:
            pairs = zip(letters, freq)
            return dict(pairs)
        return letters, freq

    def getSortedList(self):
        letters = []
        freq = []
        current = self.list.headNode
        while current != None:
            letters.append(current.char)
            freq.append(current.freq)
            current = current.nextNode
        return letters, freq

    def __str__(self):
        return "<Frequency Object>"
