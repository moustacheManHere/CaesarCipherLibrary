class CipherText:
    def __init__(self,text):
        self.txt = text
        self.key =None
    
    def getText(self):
        return self.txt
    
    def getKey(self):
        return self.key
    
    def __str__(self):
        return f"<CipherText Object: {self.txt}>"