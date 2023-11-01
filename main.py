from classes.basecipher import CipherText


def printMessage():
    header = """
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
    print(header)


def printChoice():
    menu = """
Please select your choice: (1, 2, 3, 4, 5, 6, 7, 8)
    1. Encrypt/Decrypt Message
    2. Encrypt/Decrypt File
    3. Analyze letter frequency distribution
    4. Infer Caesar cipher key from file
    5. Analyze, and sort encrypted files
    6. Extra Option One
    7. Extra Option Two
    8. Exit
"""
    print(menu)


def process_cipher_operation(inputStr):
    encrypt = inputStr == "E" or inputStr == "e"
    operation = "encrypt" if encrypt else "decrypt"
    text = input(f"\nPlease type in the text you want to {operation}:\n")
    key = input("\nEnter the cipher key: ")
    textObj = CipherText(text)
    print(f"\nPlaintext:\t{textObj.txt}")
    if encrypt:
        textObj.encrypt(key)
    else:
        textObj.decrypt(key)
    print(f"Ciphertext:\t{textObj.txt}")


def main():

    input("\nPress enter key, to continue....  ")
    printChoice()
    choice = input("Enter choice: ")

    try:
        choice = int(choice)
    except:
        print("Please enter a number.")
        main()

    if not choice in range(1, 9):
        print("Sorry invalid number entered... Please try again.")
        main()

    if choice == 1:
        choice = "f"
        tries = 0  # give them three tries only to avoid infinite loops
        while choice not in ["E", "D", "e", "d"] and tries < 3:
            choice = input('\nEnter "E" for Encrypt or "D" for Decrypt: ')
            tries += 1
        process_cipher_operation(choice)
        main()


if __name__ == "__main__":
    printMessage()
    main()
    print(
        "\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer"
    )
