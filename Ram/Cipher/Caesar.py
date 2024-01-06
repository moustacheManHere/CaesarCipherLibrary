from Ram.Base.Cipher import CipherText


class Caesar(CipherText):
    def encrypt(self, key):
        key = key % 26
        result = ""
        for char in self.txt:
            shifted_char = char
            if char.isalpha():
                shifted_char = chr(
                    (ord(char) - ord("A" if char.isupper() else "a") + key) % 26
                    + ord("A" if char.isupper() else "a")
                )
            result += shifted_char
        self.txt = result
        return self

    def decrypt(self, key):
        key = key % 26
        key = key * -1
        result = ""
        for char in self.txt:
            if char.isalpha():
                shifted_char = chr(
                    (ord(char) - ord("A" if char.isupper() else "a") + key) % 26
                    + ord("A" if char.isupper() else "a")
                )
                result += shifted_char
            else:
                result += char
        self.txt = result
        return self
