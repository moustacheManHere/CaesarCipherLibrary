from Ram.Base.Cipher import CipherText


class VigText(CipherText):
    def __init__(self, text):
        super().__init__(text)

    def encrypt(self, key):
        result = ""
        for char in self.txt:
            if char.isalpha():
                tempkey = key.headNode.char
                case_offset = ord("A") if char.isupper() else ord("a")
                key_offset = ord(tempkey.upper()) - ord("A")

                shifted = (ord(char) - case_offset + key_offset) % 26 + case_offset
                result += chr(shifted)
                key.headNode = key.headNode.nextNode
            else:
                result += char
        self.txt = result
        self.key = key

    def decrypt(self, key):
        result = ""
        for char in self.txt:
            if char.isalpha():
                tempkey = key.headNode.char
                case_offset = ord("A") if char.isupper() else ord("a")
                key_offset = ord(tempkey.upper()) - ord("A")
                key_offset = -key_offset
                shifted = (ord(char) - case_offset + key_offset) % 26 + case_offset
                result += chr(shifted)
                key.headNode = key.headNode.nextNode
            else:
                result += char
        self.txt = result
        self.key = key
