import os


class FileHandler:
    def readFile(self, filename):
        try:
            with open(filename, "r") as file:
                text = file.read()
        except:
            print("Warning: File wasn't read. An default string will be used instead.")
            text = "Lol how did you get here"
        return text

    def ifFileExists(self, filename):
        return os.path.isfile(filename)

    def ifFolderExists(self, folder):
        if not os.path.isdir(folder):
            print("Error: Folder not found!")
            return False
        elif not os.access(folder, os.W_OK):
            print(f"Error: No write permission for {folder}.")
            return False
        return True

    def isWritable(self, filename):
        try:
            yes = open(filename, "w")
            return True
        except:
            return False

    def extractFilesWithExt(self, folder, extensions):
        files = os.listdir(folder)
        if not any(file.lower().endswith(tuple(extensions)) for file in files):
            return None
        accepted_files = [
            os.path.join(folder, file)
            for file in files
            if file.lower().endswith(tuple(extensions))
        ]
        return accepted_files

    def saveFile(self, text, filename):
        try:
            with open(filename, "w") as file:
                file.write(text)
            return True
        except:
            print("Warning: File couldn't be written.")
            return False

    def saveCipher(self, cipher, filename):

        try:
            with open(filename, "w") as file:
                file.write(cipher.getText())
            return True
        except:
            print("Warning: File couldn't be written.")
            return False

    def readFreqFile(self, filename="Ram/Static/eng.txt"):
        array = []
        from Ram.Validate.File import FileValidator

        fileValidate = FileValidator()
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
        except:
            print("Warning: File wasn't read. Using Default.")
            array = self.readFreqFile("Ram/Static/eng.txt")
        try:
            array = []
            for i in lines:
                array.append(i.split(",")[:2])
        except:
            print("Error: Couldn't parse given frequencies file. Using Default")
            array = self.readFreqFile("Ram/Static/eng.txt")
        output = fileValidate.freqFile(array)

        if output is None:
            print(
                "\nWarning: Couldn't parse given frequencies file. Using Default Frequencies"
            )
            output = self.readFreqFile("Ram/Static/eng.txt")

        return output

    def readTextFrequency(self, filename):
        txt = self.readFile(filename)
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string = "".join(char.upper() for char in txt if char.upper() in alpha)
        freqDict = {}

        for i in string:
            if i not in freqDict:
                freqDict[i] = 1
            else:
                freqDict[i] += 1
        letterCount = len(freqDict.keys())
        for i in alpha:
            if i not in freqDict:
                freqDict[i] = 0
        if letterCount != 0:
            freq = [
                value / sum(list(freqDict.values())) * 100
                for value in list(freqDict.values())
            ]
            letters = list(freqDict.keys())
        else:
            freq = [0] * 26
            letters = list(freqDict.keys())
        return letters, freq

    def __str__(self):
        return "<File Handler Object>"
