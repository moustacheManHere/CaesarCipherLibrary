class CipherText:
    def __init__(self, txt):
        self.txt = txt

    def __str__(self) -> str:
        return f"<CipherText Object = '{self.txt}' >"

    def encrypt(self, key):
        try:
            key = int(key)
        except:
            print(
                "Warning! A valid key was not provided for this string and thus cannot be encrypted!"
            )
            return self

        if not isinstance(self.txt, str):
            print(
                "Warning! this object was not initialised with a string and thus cannot be encrypted!"
            )
            return self

        result = "".join(
            chr(
                (ord(char) - ord("A" if char.isupper() else "a") + key)
                % 26  
                + ord("A" if char.isupper() else "a")  
            )
            if char.isalpha()
            else char
            for char in self.txt 
        )
        self.txt = result
        return self

    def decrypt(self, key):

        try:
            key = int(key)
        except:
            print(
                "Warning! A valid key was not provided for this string and thus cannot be encrypted!"
            )
            return self

        if not isinstance(self.txt, str):
            print(
                "Warning! this object was not initialised with a string and thus cannot be encrypted!"
            )
            return self

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
        return self
