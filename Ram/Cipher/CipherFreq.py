from Ram.Cipher.CipherFile import CipherFile

class CipherFreq(CipherFile):
    def calcFreq(self):
        input_string = self.txt.lower()
        letter_counts = {}
        total_letters = 0

        for char in input_string:
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1
                total_letters += 1
        letter_frequencies = {}
        for letter in "abcdefghijklmnopqrstuvwxyz":
            count = letter_counts.get(letter, 0)
            frequency_percentage = round((count / total_letters) * 100,2)
            letter_frequencies[letter] = frequency_percentage
        return letter_frequencies
    def getTopFreq(self):
        return  dict(sorted(self.calcFreq().items(), key=lambda x: x[1], reverse=True)[:5])