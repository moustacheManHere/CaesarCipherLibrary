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