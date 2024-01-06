from Ram.IO.File import FileHandler
import math
import os
from Ram.Stat.Frequency import Frequency
from Ram.Base.Cipher import CipherText


class OutputHandler:
    def __init__(self):
        self.file = FileHandler()

    def print_start(self):
        os.system("cls" if os.name == "nt" else "clear")
        start = self.file.readFile("Ram/Static/start.txt")
        print(start)

    def print_options(self):
        print("")
        options = self.file.readFile("Ram/Static/options.txt")
        print(options)

    def print_end(self):
        print("")
        end = self.file.readFile("Ram/Static/end.txt")
        print(end)

    def cipherTextOutput(self, cipher, key, isEncrypt=True):
        if not isinstance(cipher, CipherText):
            return
        if isEncrypt:
            print(f"\nPlaintext:\t{cipher.getText()}")
            cipher.encrypt(key)
            print(f"Cipher:\t\t{cipher.getText()}")
        else:
            print(f"Cipher:\t\t{cipher.getText()}")
            cipher.decrypt(key)
            print(f"Plaintext:\t{cipher.getText()}")

    def printFreq(self, freqObj):
        if not isinstance(freqObj, Frequency):
            print("Typeerror: Object sent for printing not is not of type Frequency")

        letter_frequencies = freqObj.getAlphaList(toround=2, todict=True)
        top_5_letters = freqObj.getTopLetters(toround=2, todict=True,top=6)

        printArray = []
        alpha = list(letter_frequencies.keys())
        for i in range(len(alpha) + 2):
            printArray.append([" "] * len(alpha) * 3)

        for i in range(len(alpha) * 3):
            if i % 3 == 0:
                printArray[-1][i] = alpha[int(i / 3)].capitalize()
            if i != len(alpha) * 3 - 1:
                printArray[-2][i] = "_"

        for i in range(len(printArray) - 1):
            if i != len(printArray) - 2:
                printArray[i][
                    -1
                ] = f"| {alpha[i].capitalize()}- {letter_frequencies[alpha[i]]}%"
            else:
                printArray[i][-1] = "|"

        sideArray = ["TOP 5 FREQ", "----------"] + [
            f"| {i.capitalize()}- {top_5_letters[i]} %" for i in top_5_letters.keys()
        ]

        for i in range(10, 18):
            printArray[i].append("\t\t" + sideArray[i - 10])

        starArr = []
        for i in alpha:
            starArr.append(math.ceil((letter_frequencies[i]) / 100 * 26))

        for i, v in enumerate(starArr):
            verticalIndex = i * 3
            for k in range(v):
                printArray[25 - k][verticalIndex] = "*"

        [print("".join(i)) for i in printArray]

    def bulkOutput(self, sortedList):
        current = sortedList.headNode
        fileNum = 1
        log = ""
        if current == None:
            return
        path = current.getFileName()
        folder = os.path.dirname(path)
        while current != None:
            path = current.getFileName()
            newFile = "file" + str(fileNum) + ".txt"
            newpath = os.path.join(folder, newFile)
            key = current.getKey()
            filename = os.path.basename(path)
            printStr = f"Decrypting: {(filename)} with key: {key} as: {newFile}\n"
            log += printStr + "\n"
            print(printStr)
            self.file.saveCipher(current, newpath)
            current = current.nextNode
            fileNum += 1
        logPath = os.path.join(folder, "log.txt")
        self.file.saveFile(log, logPath)

    def __str__(self):
        return "<Output Handler Object>"
