from Ram.IO.InputHandler import InputHandler
from Ram.Base.Processor import CipherProcessor
from Ram.IO.OutputHandler import OutputHandler

class CipherCLI:
    def __init__(self):
        self.processor = CipherProcessor()
        self.inputter = InputHandler()
        self.output = OutputHandler()

    def run(self):
        
        self.output.print_choice()

        choice = self.inputter.getIntInput("choice", range(1, 9))
        if choice is None:
            self.run()

        if choice == 1:
            self.getEncDecInput(self.processor.process_cipher_operation)
            self.run()

        elif choice == 2:
            self.getEncDecInput(self.processor.process_cipher_file)
            self.run()

    def getEncDecInput(self,func):
        first_choice = self.inputter.getStrInput('\nEnter "E" for Encrypt or "D" for Decrypt: ', ["E", "D", "e", "d"])
        if first_choice is not None:
            func(first_choice)

