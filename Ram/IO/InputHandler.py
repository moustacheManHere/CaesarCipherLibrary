import os

class InputHandler:
    def getIntInput(self, name, num_range=None):
        key = "lolzz"
        tries = 0
        while not isinstance(key, int) and tries < 3:
            key = input(f"\nEnter {name}: ")
            try:
                key = int(key)
            except ValueError:
                print("Error: Please enter a valid number.")
            tries += 1
        if tries == 3 and not isinstance(key, int):
            print(f"Error: Failed to receive a valid {name}. Exiting...")
            return None
        if num_range is not None and key not in num_range:
            print("Error: An invalid number entered. Please try again.")
            return None
        return key

    def getStrInput(self, prompt, accept):
        choice = "f"
        tries = 0 
        while choice not in accept and tries < 3:
            choice = input(prompt)
            tries += 1
        if tries == 3 and choice not in accept:
            print("\nError: Failed to receive a valid choice.")
            return None
        else:
            return choice

    def getFilename(self, prompt):
        tries = 0
        while tries < 3:
            filename = input(prompt)
            tries += 1
            if not os.path.isfile(filename):
                print(f"Error: The file path {filename} does not exist.")
            elif not os.access(filename, os.W_OK):
                print(f"Error: No write permission for {filename}.")
            else:
                return filename
        return None

    def encryptDecryptHandler(self, input_str, name):
        encrypt = input_str.lower() == "e"
        operation = "encrypt" if encrypt else "decrypt"
        if name == "file":
            text = self.getFilename(f"\nPlease type in the {name} you want to {operation}:\n")
            if text is None:
                print("Error: Valid filename not received! Exiting...")
                return None, None, None
        else:
            text = input(f"\nPlease type in the {name} you want to {operation}:\n")
        key = self.getIntInput("key", None)
        return key, text, encrypt

    def getNewFileName(self):
        file_path = input(f"\nPlease enter an output file: ")
        try:
            open(file_path, 'w')
        except:
            print("Error: Invalid Filename!")
            return None
        if not os.path.exists(file_path):
            print("Error: Invalid file name.")
            return None
        if not file_path.endswith(".txt"):
            print("Warning: Not a text file! May not be readable later.")
        if not os.access(file_path, os.W_OK):
            print("Error: No write permission for the file.")
            return None
        return file_path
