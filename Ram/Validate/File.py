from Ram.IO.File import FileHandler
import os


class FileValidator:
    def __init__(self):
        self.fileHandle = FileHandler()
        self.reserved = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
    def freqFile(self, array):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if len(array) > 26:
            print("Warning: More rows than expected. Taking only the first 26.")
            array = array[:26]
        if len(array) < 26:
            print(
                "Warning: Some letters are missing from frequency file. Filling in zero for missing letters."
            )
        letters = []
        freq = []
        for v, i in enumerate(array):
            if len(i) != 2:
                print(
                    f"Error: Less than 2 columns detected at line {v+1}. Plase fill in and try again."
                )
                return None
            if not isinstance(i[0], str):
                print(f"Error: First column value at line {v+1} is not a string")
                return None
            if len(i[0]) != 1:
                print(
                    f"Warning: First column contains non-char value at line {v+1}. Only the first letter of it is used. Please change or it may lead to unexpected results."
                )
                i[0] = i[0][0]
            if i[0].upper() not in alpha:
                print(f"Error: First column value at line {v+1} is not a alphabet")
                return None
            letters.append(i[0].upper())
            try:
                if i[1].endswith("\n"):
                    i[1] = i[1].rstrip("\n")
                i[1] = float(i[1])
                freq.append(i[1])
            except:
                print(
                    f"Error: Unable to convert frequency value at line {v} into a float"
                )
                return None
        if len(letters) != len(set(letters)):
            print(
                "Warning! Duplicates found in frequencies provided. Please fix it as frequencies removed may be unpredictable!"
            )
            letter_freq_pairs = list(zip(letters, freq))
            unique_letters = list(set(letters))
            unique_pairs = [
                (letter, freq)
                for letter, freq in letter_freq_pairs
                if letter in unique_letters
            ]
            letters, freq = zip(*unique_pairs)
        if len(letters) != len(alpha):
            missing = set(alpha) - set(letters)
            for i in missing:
                letters.append(i)
                freq.append(0)
        return letters, freq

    def filename(self, user_input, extensions=[".txt"], mustexist=True):
        user_input = user_input.strip()
        validExt = any(user_input.lower().endswith(ext) for ext in extensions)
        if not validExt:
            print("\nError: This file extension is not yet supported.")
            return None
        if mustexist and not self.fileHandle.ifFileExists(user_input):
            print("\nError: File does not exist!")
            return None
        filename = os.path.basename(user_input)
        base_name = os.path.splitext(filename)[0].upper()
        if base_name in self.reserved:
            print("Do not use reserved names you idiot!")
            return None
        return user_input

    def foldername(self, user_input, extensions=[".txt"], mustexist=True):

        user_input = user_input.strip()
        if not mustexist:
            try:
                os.makedirs(user_input)
                print(f"Directory '{user_input}' created successfully.")
            except OSError as e:
                print(f"Error creating directory '{user_input}': {e}")
            return user_input
        if not self.fileHandle.ifFolderExists(user_input):
            print("Folder not found!")
            return None
        accept = self.fileHandle.extractFilesWithExt(user_input, extensions)
        accept = [i for i in accept if os.path.basename(i)[0] not in self.reserved]
        if accept == None:
            print("Error: Folder does not contain files of desired types.")
            return None
        return accept

    def __str__(self):
        return "<File Validation Object>"
