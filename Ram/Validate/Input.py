from Ram.IO.File import FileHandler


class InputValidator:
    def __init__(self):
        self.fileHandle = FileHandler()

    def integer(self, user_input, num_range=None, isInteger=True):
        user_input = user_input.strip()
        try:
            if isInteger:
                user_input = int(user_input)
            else:
                user_input = float(user_input)
        except:
            print("\nError: Unable to convert user input to number.")
            return None
        if num_range is not None and user_input not in num_range:
            print(user_input, num_range)
            print("\nError: Number not within acceptable range.")
            return None
        return user_input

    def anystring(self, user_input, accept=None, acceptEmpty=False):
        user_input = user_input.strip()
        try:
            cleaned_string = "".join(
                char
                for char in user_input
                if char.isalnum() or char.isspace() or char in ",.?!;:-"
            )
        except:
            print("\nError: Unable to parse given string.")
            return None
        if not acceptEmpty and cleaned_string == "":
            print("\nError: Empty strings or invalid characters are not accepted")
            return None
        if accept is not None and cleaned_string not in accept:
            print("\nError: String not in acceptable values.")
            return None
        return cleaned_string

    def string(self, user_input, accept=None, acceptEmpty=False):
        user_input = user_input.strip()
        try:
            cleaned_string = "".join(char for char in user_input if char.isalpha())
        except:
            print("\nError: Unable to parse given string.")
            return None
        if not acceptEmpty and cleaned_string == "":
            print("\nError: Empty strings or invalid characters are not accepted")
            return None
        if accept is not None and cleaned_string not in accept:
            print("\nError: String not in acceptable values.")
            return None
        return cleaned_string

    def vigenere(self, user_input):
        user_input = user_input.strip()
        try:
            cleaned_string = "".join(
                char for char in user_input if char.isalpha() or char.isdigit()
            )
        except:
            print("\nError: Unable to parse given string.")
            return None
        if cleaned_string == "":
            print("\nError: Empty strings or invalid characters are not accepted")
            return None
        if len(cleaned_string) > 10:
            print(
                "The key you entered is long and maybe be hard to break if you forget it."
            )
        return cleaned_string

    def __str__(self):
        return "<Input Validation Object>"
