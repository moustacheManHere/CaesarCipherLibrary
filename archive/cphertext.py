class CipherText:
    def __init__(self,txt):
        self.txt = txt
        self.currentShift = 0
    def isDecrypt(self):
        return self.currentShift == 0
    def encrypt(self,key):
        if not isinstance(self.txt, str):
            print("Warning! this object was not initialised with a string and thus cannot be encrypted!")
            return self
        if not self.isDecrypt():
            print("Warning: This string is already encrypted! Multiple encryptions will lead to complications!")
        result = "".join(
            chr(
                (ord(char) - ord("A" if char.isupper() else "a") + key) % 26 # position in ascii
                + ord("A" if char.isupper() else "a") # ascii value
            )
            if char.isalpha() else char for char in self.txt # only convert if its alphabet
        )
        self.txt = result
        self.currentShift += key
        return self
    def decrypt(self,key):

        if key is None:
            key = self.currentShift
        if not isinstance(self.txt, str):
            print("Warning! this object was not initialised with a string and thus cannot be encrypted!")
            return self
        if self.isDecrypt():
            print("Warning: This string is already decrypted!")
        
        result = "".join(
        chr(
            (ord(char) - ord("A" if char.isupper() else "a") - key) % 26
            + ord("A" if char.isupper() else "a")
        )
        if char.isalpha()
        else char
        for char in self.txt
    )
        self.txt = result
        self.currentShift -= key
        return self

