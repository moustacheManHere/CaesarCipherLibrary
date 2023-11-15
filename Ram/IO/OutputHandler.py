import math
class OutputHandler:
    def __init__(self):
        self.HEADER = """
        *********************************************************
        * ST1507 DSAA: Welcome to:                              *
        *                                                       *
        *     ~ Caesar Cipher Encrypted Message Analyzer ~      *
        *-------------------------------------------------------*
        *                                                       *
        *  - Done by: Jeyakumar Sriram(2214618)                 *
        *  - Class DAAA/2B/01                                   *
        *********************************************************
        """

        self.MENU = """
        Please select your choice: (1, 2, 3, 4, 5, 6, 7, 8)
            1. Encrypt/Decrypt Message
            2. Encrypt/Decrypt File
            3. Analyze letter frequency distribution
            4. Infer Caesar cipher key from file
            5. Analyze and sort encrypted files
            6. Extra Option One
            7. Extra Option Two
            8. Exit
        """
        self.END_TEXT = "\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer"

    def print_message(self):
        print(self.HEADER)

    def print_choice(self):
        input("\nPress enter to continue....  ")
        print(self.MENU)
        
    def print_end(self):
        print(self.END_TEXT)

    def cipherTextOutput(self,text_obj,key,encrypt):
        print(f"\nPlaintext:\t{text_obj.txt}")
        try:
            if encrypt:
                text_obj.encrypt(key)
            else:
                text_obj.decrypt(key)
            print(f"Ciphertext:\t{text_obj.txt}")
        except:
            print("Warning: Failed to encrypt/decrypt given text! Exiting...")
        

    def cipherFileOutput(self,text_obj,key,encrypt,new_filename):
        try:
            if encrypt:
                text_obj.encryptFile(new_filename, key)
            else:
                text_obj.decryptFile(new_filename, key)
        except:
            print("Warning: Failed to encrypt/decrypt given file! Exiting...")
    def printGraph(self,letter_frequencies,top_5_letters):
        printArray = []
        alpha = list(letter_frequencies.keys())
        for i in range(len(alpha)+2):
            printArray.append([" "]*len(alpha)*3)

        for i in range(len(alpha)*3):
            if i % 3 == 0:
                printArray[-1][i] = alpha[int(i/3)].capitalize()
            if i != len(alpha)*3 - 1:
                printArray[-2][i] = "_"

        for i in range(len(printArray) - 1):
            if i != len(printArray) - 2:
                printArray[i][-1] = f"| {alpha[i].capitalize()}- {letter_frequencies[alpha[i]]}%"
            else:
                printArray[i][-1] = "|"

        sideArray = ["TOP 5 FREQ", "----------"] + [f"| {i.capitalize()}- {top_5_letters[i]} %" for i in top_5_letters.keys()]

        for i in range(10,17):
            printArray[i].append("\t\t"+sideArray[i-10])

        starArr = []
        for i in alpha:
            starArr.append(math.ceil((letter_frequencies[i])/100*26))


        for i,v in enumerate(starArr):
            verticalIndex = i * 3
            for i in range(v):
                printArray[25-i][verticalIndex] = "*"

        # print everything
        [print("".join(i)) for i in printArray]