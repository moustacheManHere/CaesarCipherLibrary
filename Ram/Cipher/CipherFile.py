from Ram.Cipher.CipherText import CipherText

class CipherFile(CipherText):
    def __init__(self,filename):
        try:
            with open(filename, "r") as file:
                text = file.read()
        except:
            print("Warning file wasnt read")
            text = ""
        super().__init__(text)
    def encryptFile(self, newFile, key):
        super().encrypt(key)
        with open(newFile, 'w') as file:
            file.write(self.txt)
        return 1
    def decryptFile(self, newFile, key):
        super().decrypt(key)
        with open(newFile, 'w') as file:
            file.write(self.txt)
        return 1
