from Ram.IO.InputHandler import InputHandler
from Ram.Cipher.CipherFile import CipherFile
from Ram.Cipher.CipherText import CipherText
from Ram.IO.OutputHandler import OutputHandler
from Ram.Cipher.CipherFreq import CipherFreq
from Ram.Cipher.CipherBrute import CipherBrute

class CipherProcessor:
    def __init__(self):
        self.inputter = InputHandler()
        self.outputter = OutputHandler()

    def process_cipher_operation(self, input_str):
        key, text, encrypt = self.inputter.encryptDecryptHandler(input_str,"text")
        if key is None:
            return 0
        text_obj = CipherText(text)
        self.outputter.cipherTextOutput(text_obj,key,encrypt)

    def process_cipher_file(self, input_str):
        key, filename, encrypt = self.inputter.encryptDecryptHandler(input_str,"file")
        if key is None or not filename:
            return 0

        text_obj = CipherFile(filename)
        new_filename = self.inputter.getNewFileName()
        if new_filename == 0:
            return 0
        self.outputter.cipherFileOutput(text_obj,key,encrypt,new_filename)
    def showFreqStat(self):
        filename = self.inputter.getFilename("Please enter the filename: ")
        if not filename:
            return 0
        text_obj = CipherFreq(filename)
        letter_frequencies = text_obj.calcFreq()
        top_5_letters = text_obj.getTopFreq()
        self.outputter.printGraph(letter_frequencies,top_5_letters)

    def BruteForceFile(self):
        filename = self.inputter.getFilename("\nPlease enter the file to analyze: ")
        if not filename:
            return 0
        refFilename = self.inputter.getFilename("\nPlease enter the reference frequencies file: ")
        if not filename:
            return 0
        
        text_obj = CipherBrute(filename,refFilename)
        key = text_obj.breakCipher()
        print("The inferred caesar cipher key is: ",key)
        choice = self.inputter.getStrInput("Would you want to decrypt this file using this key? y/n: ",
                                           ["y","n"])
        if not choice or choice == "n":
            return 0
        
        new_filename = self.inputter.getNewFileName()
        if new_filename == 0:
            return 0
        self.outputter.cipherFileOutput(text_obj,key,False,new_filename)

