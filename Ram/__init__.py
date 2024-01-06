# Handle IO
from Ram.IO.Output import OutputHandler
from Ram.IO.File import FileHandler
from Ram.IO.Input import InputHandler

# Validate User Input
from Ram.Validate.Input import InputValidator
from Ram.Validate.File import FileValidator

# Nodes
from Ram.Nodes.Letter import LetterNode
from Ram.Nodes.File import CaesarFileNode

# Cipher
from Ram.Cipher.Caesar import Caesar
from Ram.Cipher.Vigenere import VigText

# Files
from Ram.Files.Custom import LigmaFile
from Ram.Files.Caesar import CaeserFile

# Statistics
from Ram.Stat.Frequency import Frequency

# Lists
from Ram.Lists.Sorted import SortedList
from Ram.Lists.Circular import CircularLL

# Miscellaneous
import os


class GetsFullMarks:
    def __init__(self):
        self.file = FileHandler()
        self.output = OutputHandler()
        self.input = InputHandler()
        self.inpValidate = InputValidator()
        self.fileValidate = FileValidator()
        self.REQUIRED_FILES = [
            "Ram/Static/end.txt",
            "Ram/Static/eng.txt",
            "Ram/Static/options.txt",
            "Ram/Static/start.txt",
        ]

    def checkVitals(self):
        for i in self.REQUIRED_FILES:
            if not self.file.ifFileExists(i):
                print(
                    f"\nError: {i} is missing from Ram/Static. Please create the file and rerun the program\n"
                )
                return None
        return "Lets gooooo"

    def run(self):
        self.input.getThreeTriesInput("\nPress enter to continue....  ")
        self.output.print_options()
        choice = self.input.getThreeTriesInput(
            "Enter choice: ",
            error="Sorry, a valid input wasn't received. Exiting...",
            validator=self.inpValidate.integer,
            num_range=range(1, 9),
            errorAction=self.run,
        )

        if choice == 1:
            twoChoice = self.input.getThreeTriesInput(
                '\nEnter "E" for Encrypt or "D" for Decrypt: ',
                error="Sorry. A valid choice was not received.",
                validator=self.inpValidate.string,
                accept=["E", "D", "e", "d"],
                errorAction=self.run,
            )

            toEncrypt = twoChoice.upper() == "E"
            operation = "encrypt" if toEncrypt else "decrypt"

            textInput = self.input.getThreeTriesInput(
                f"\nPlease type in the text you want to {operation}: \n",
                error="Exiting this choice...",
                validator=self.inpValidate.anystring,
                errorAction=self.run,
            )

            cipher = Caesar(textInput)
            key = self.input.getThreeTriesInput(
                "\nEnter the cipher key: ",
                error="Sorry, a valid key was not received, exiting...",
                validator=self.inpValidate.integer,
                errorAction=self.run,
            )

            self.output.cipherTextOutput(cipher, key, toEncrypt)
            self.run()

        elif choice == 2:
            twoChoice = self.input.getThreeTriesInput(
                '\nEnter "E" for Encrypt or "D" for Decrypt: ',
                error="Sorry. A valid choice was not received.",
                validator=self.inpValidate.string,
                accept=["E", "D", "e", "d"],
                errorAction=self.run,
            )

            toEncrypt = twoChoice.upper() == "E"
            operation = "encrypt" if toEncrypt else "decrypt"

            filename = self.input.getThreeTriesInput(
                f"\nPlease enter the file you want to {operation}: ",
                error="Sorry. A valid input filename was not received.",
                validator=self.fileValidate.filename,
                errorAction=self.run,
            )

            text = self.file.readFile(filename)
            key = self.input.getThreeTriesInput(
                "\nEnter the cipher key: ",
                error="Sorry, a valid key was not received, exiting...",
                validator=self.inpValidate.integer,
                errorAction=self.run,
            )

            filename = self.input.getThreeTriesInput(
                f"\nPlease enter a output file: ",
                error="Sorry. A valid output filename was not received.",
                validator=self.fileValidate.filename,
                mustexist=False,
                errorAction=self.run,
            )

            if self.file.ifFileExists(filename):
                twoChoice = self.input.getThreeTriesInput(
                    "\nWarning: A file already exists at this location and will be overwritten. Continue (y/n) ? ",
                    error="Sorry. A valid choice was not received.",
                    validator=self.inpValidate.string,
                    accept=["y", "n"],
                    errorAction=self.run,
                )
                if twoChoice == "n":
                    self.run()

            cipher = Caesar(text)
            if toEncrypt:
                cipher.encrypt(key)
            else:
                cipher.decrypt(key)

            self.file.saveCipher(cipher, filename)
            self.run()

        elif choice == 3:
            filename = self.input.getThreeTriesInput(
                f"\nPlease enter the file you want to analyze: ",
                error="Sorry. A valid input filename was not received.",
                validator=self.fileValidate.filename,
                errorAction=self.run,
            )
            print("")
            freqObj = Frequency(filename)
            self.output.printFreq(freqObj)
            self.run()

        elif choice == 4:
            analyzeFile = self.input.getThreeTriesInput(
                f"\nPlease enter the file you want to analyze: ",
                error="Sorry. A valid input filename was not received.",
                validator=self.fileValidate.filename,
                errorAction=self.run,
            )

            text = self.file.readFile(analyzeFile)
            cipher = Caesar(text)

            refFile = self.input.getThreeTriesInput(
                f"\nPlease enter the reference frequencies file: ",
                error="Sorry. A valid input filename was not received.",
                validator=self.fileValidate.filename,
                errorAction=self.run,
            )

            cipherFile = CaeserFile(analyzeFile)
            freqFile = Frequency(refFile, freqFile=True)
            cipherFile.breakCaesar(freqFile)
            print(f"The inferred caesar cipher key is: {cipherFile.key}")
            twoChoice = self.input.getThreeTriesInput(
                "\nWould you want to decrypt this file using this key? (y/n): ",
                error="Sorry. A valid choice was not received.",
                validator=self.inpValidate.string,
                accept=["y", "n"],
                errorAction=self.run,
            )
            if twoChoice == "n":
                self.run()
            filename = self.input.getThreeTriesInput(
                f"\nPlease enter a output file: ",
                error="Sorry. A valid output filename was not received.",
                validator=self.fileValidate.filename,
                mustexist=False,
                errorAction=self.run,
            )

            if self.file.ifFileExists(filename):
                twoChoice = self.input.getThreeTriesInput(
                    "\nWarning: A file already exists at this location and will be overwritten. Continue (y/n) ? ",
                    error="Sorry. A valid choice was not received.",
                    validator=self.inpValidate.string,
                    accept=["y", "n"],
                    errorAction=self.run,
                )
                if twoChoice == "n":
                    self.run()
            self.file.saveCipher(cipherFile, filename)
            self.run()
        elif choice == 5:
            folderFiles = self.input.getThreeTriesInput(
                f"\nPlease enter the folder name: ",
                error="Sorry. A valid input folder was not received.",
                validator=self.fileValidate.foldername,
                errorAction=self.run,
            )
            freqFile = Frequency("Ram/Static/eng.txt", freqFile=True)
            sortedList = SortedList()
            for i in folderFiles:
                file = CaesarFileNode(i, freqFile)
                sortedList.insert(file)
            self.output.bulkOutput(sortedList)
            self.run()

        elif choice == 6:
            twoChoice = self.input.getThreeTriesInput(
                '\nEnter "E" for Encrypt or "D" for Decrypt: ',
                error="Sorry. A valid choice was not received.",
                validator=self.inpValidate.string,
                accept=["E", "D", "e", "d"],
                errorAction=self.run,
            )

            toEncrypt = twoChoice.upper() == "E"
            operation = "encrypt" if toEncrypt else "decrypt"

            filename = self.input.getThreeTriesInput(
                f"\nPlease enter the file you want to {operation}: ",
                error="Sorry. A valid input filename was not received.",
                validator=self.fileValidate.filename,
                errorAction=self.run,
            )

            text = self.file.readFile(filename)
            vcipher = VigText(text)
            key = self.input.getThreeTriesInput(
                "\nEnter the vignere cipher key (Only alphabets no spacing): ",
                error="Sorry, a valid key was not received, exiting...",
                validator=self.inpValidate.vigenere,
                errorAction=self.run,
            )
            keyList = CircularLL()
            keyList.insertAll(key, LetterNode)
            filename = self.input.getThreeTriesInput(
                f"\nPlease enter a output file: ",
                error="Sorry. A valid output filename was not received.",
                validator=self.fileValidate.filename,
                mustexist=False,
                errorAction=self.run,
            )

            if self.file.ifFileExists(filename):
                twoChoice = self.input.getThreeTriesInput(
                    "\nWarning: A file already exists at this location and will be overwritten. Continue (y/n) ? ",
                    error="Sorry. A valid choice was not received.",
                    validator=self.inpValidate.string,
                    accept=["y", "n"],
                    errorAction=self.run,
                )
                if twoChoice == "n":
                    print("Alright that's fine too! Exiting...")
                    self.run()
            if toEncrypt:
                vcipher.encrypt(keyList)
            else:
                vcipher.decrypt(keyList)

            self.file.saveCipher(vcipher, filename)
            self.run()
        elif choice == 7:
            twoChoice = self.input.getThreeTriesInput(
                '\nEnter "E" for Encrypt or "D" for Decrypt: ',
                error="Sorry. A valid choice was not received.",
                validator=self.inpValidate.string,
                accept=["E", "D", "e", "d"],
                errorAction=self.run,
            )

            toEncrypt = twoChoice.upper() == "E"
            operation = "encrypt" if toEncrypt else "decrypt"
            if toEncrypt:
                folderFiles = self.input.getThreeTriesInput(
                    f"\nPlease enter the folder name: ",
                    error="Sorry. A valid input folder was not received.",
                    validator=self.fileValidate.foldername,
                    errorAction=self.run,
                )
            else:
                filename = self.input.getThreeTriesInput(
                    f"\nPlease enter the file you want to {operation}: ",
                    error="Sorry. A valid input filename was not received.",
                    validator=self.fileValidate.filename,
                    errorAction=self.run,
                    extensions=[".ligma"],
                )
            key = self.input.getThreeTriesInput(
                "\nEnter the vignere cipher key (Only alphabets no spacing): ",
                error="Sorry, a valid key was not received, exiting...",
                validator=self.inpValidate.vigenere,
                errorAction=self.run,
            )
            keyObj = CircularLL()
            keyObj.insertAll(key, LetterNode)
            if toEncrypt:
                filename2 = self.input.getThreeTriesInput(
                    f"\nPlease enter a output file: ",
                    error="Sorry. A valid output filename was not received.",
                    validator=self.fileValidate.filename,
                    mustexist=False,
                    errorAction=self.run,
                    extensions=[".ligma"],
                )
                if self.file.ifFileExists(filename2):
                    twoChoice = self.input.getThreeTriesInput(
                        "\nWarning: A file already exists at this location and will be overwritten. Continue (y/n) ? ",
                        error="Sorry. A valid choice was not received.",
                        validator=self.inpValidate.string,
                        accept=["y", "n"],
                        errorAction=self.run,
                    )
                    if twoChoice == "n":
                        self.run()
                custom = LigmaFile()
                for i in folderFiles:
                    custom.addFile(i)
                encrypted = custom.toLigma(keyObj)
                self.file.saveFile(encrypted, filename2)
            else:
                outputFolder = self.input.getThreeTriesInput(
                    f"\nPlease enter the folder name: ",
                    error="Sorry. A valid input folder was not received.",
                    validator=self.fileValidate.foldername,
                    errorAction=self.run,
                    mustexist=False,
                )
                custom = LigmaFile()

                custom.loadLigma(filename, keyObj)
                outputFiles = custom.toPlainText()
                integer = 0
                for i in outputFiles:
                    tempFile = os.path.join(outputFolder, f"file{integer}.txt")
                    self.file.saveFile(i, tempFile)
                    integer += 1
            self.run()

    def __str__(self):
        return "<Main Program Object>"
