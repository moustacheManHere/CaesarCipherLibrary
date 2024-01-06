from Ram.IO.File import FileHandler

from Ram.Cipher.Caesar import Caesar
from Ram.Lists.Circular import CircularLL
from Ram.Cipher.Vigenere import VigText
import random


class LigmaFile:
    def __init__(self):
        self.file = FileHandler()

        self.keys = []
        self.texts = []

    def addFile(self, filename):
        text = self.file.readFile(filename)
        key = random.randint(0, 25)
        self.keys.append(key)
        self.texts.append(text)

    def loadLigma(self, filename, vig):
        text = self.file.readFile(filename)

        contents = text.split("\n")
        keyString = contents[0]
        cipherTexts = contents[1:]

        keyArr = self.cipherKeys(keyString, vig, encrypt=False)

        if len(keyArr) != len(cipherTexts):
            print("Error: Some keys are missing")
            return None
        self.keys.append(keyArr)

        for i, v in enumerate(cipherTexts):
            clean = self.advancedCipher(v, keyArr[i], vig, encrypt=False)
            self.texts.append(clean)

    def toLigma(self, vig):

        finalArr = []

        keyString = self.cipherKeys(self.keys, vig)
        finalArr.append(keyString)

        for i, v in enumerate(self.texts):
            cipher = self.advancedCipher(v, self.keys[i], vig)
            finalArr.append(cipher)

        finalString = "\n".join(finalArr)
        return finalString

    def toPlainText(self):
        return self.texts

    def advancedCipher(self, text, key, vigenere, encrypt=True):
        if (
            not isinstance(text, str)
            or not isinstance(vigenere, CircularLL)
            or not isinstance(key, int)
        ):
            print(type(vigenere), type(key), type(text))
            return ""
        if encrypt:
            text = text.replace(" ", "ll{fuc*")
            text = text.replace("\n", "odj.o|")
            vigenereLen = vigenere.getLen()
            caesar_text = Caesar(text)
            caesar_text.encrypt(key + vigenereLen)
            vigText = VigText(caesar_text.getText())
            vigText.encrypt(vigenere)
            return vigText.getText()
        else:
            vigText = VigText(text)
            vigText.decrypt(vigenere)
            caesar_text = Caesar(vigText.getText())
            vigenere_len = vigenere.getLen()
            caesar_text.decrypt(key + vigenere_len)
            text = caesar_text.getText()
            text = text.replace("ll{fuc*", " ")
            text = text.replace("odj.o|", "\n")
            return text

    def cipherKeys(self, arrCaesar, vigenere, encrypt=True):
        if encrypt:
            if not isinstance(arrCaesar, (list, tuple)) or not isinstance(
                vigenere, CircularLL
            ):
                return ""
            keyString = [chr(number + ord("a")) for number in arrCaesar]
            keyString = keyString * (vigenere.getLen() + 5)
            vigenereCipher = VigText(keyString)
            vigenereCipher.encrypt(vigenere)
            return vigenereCipher.getText()
        else:
            if not isinstance(arrCaesar, str) or not isinstance(vigenere, CircularLL):
                return ""
            vigObj = VigText(arrCaesar)
            vigObj.decrypt(vigenere)
            key_string = vigObj.getText()
            vigenere_len = vigenere.getLen() + 5
            keyLen = len(arrCaesar) // vigenere_len
            key_string = key_string[:keyLen]
            arr_caesar = [(ord(char) - ord("a")) % 26 for char in key_string]
            return arr_caesar
