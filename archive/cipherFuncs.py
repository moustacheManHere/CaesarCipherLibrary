from classes.basecipher import CipherText
from classes.inputter import ThreeTriesInput
from classes.cipherFile import CipherFile
from classes.cipherProcessor import CipherProcessor


def process_cipher_operation(inputStr):
    encrypt = False
    operation = "decrypt"
    if inputStr == "E" or  inputStr == "e":
        encrypt = True
        operation = "encrypt"   
    text = input(f"\nPlease type in the text you want to {operation}:\n")
    inputter = ThreeTriesInput()
    key = inputter.getIntInput("key",None)
    if key == None:
        print("Invalid key! Exiting...")
        return 0
    textObj = CipherText(text)
    print(f"\nPlaintext:\t{textObj.txt}")
    if encrypt:
        textObj.encrypt(key)
    else:
        textObj.decrypt(key)
    print(f"Ciphertext:\t{textObj.txt}")

def process_cipher_file(inputStr):
    encrypt = inputStr == "E" or inputStr == "e"
    operation = "encrypt" if encrypt else "decrypt"    
    inputter = ThreeTriesInput()
    filename = inputter.getFilename(f"\nPlease enter the file you want to {operation}: ")
    if filename == None:
        print(f"The file path {filename} does not exist.")
        return 0
    key = inputter.getIntInput("key",None)
    if key == None:
        print("Invalid key! Exiting...")
        return 0
    textObj = CipherFile(filename)
    newFilename = input(f"\nPlease enter a output file: ")
    if encrypt:
        textObj.encryptFile(newFilename,key)
    else:
        textObj.decryptFile(newFilename,key)