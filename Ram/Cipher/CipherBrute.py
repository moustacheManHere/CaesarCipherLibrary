from Ram.Cipher.CipherFreq import CipherFreq
import numpy as np
class CipherBrute(CipherFreq):
    def __init__(self, filename,freqFile):
        super().__init__(filename)
        try:
            self.normalFreq = self.readFreqFile(freqFile)
        except:
            self.normalFreq = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 
                            0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1,
                                2.8, 0.98, 2.4, 0.15, 2.0, 0.074]
        
    def readFreqFile(self,freqFile):
        column_values = {}
        try :
            with open(freqFile, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    values = line.strip().split(',')
                    column_values[values[0].lower()] = float(values[1])
            expected = [column_values[letter] for letter in "abcdefghijklmnopqrstuvwxyz"]
            return expected
        except:
            raise FileNotFoundError
    def getChi(self,observed,expected):
        chi_square_statistic = sum(
            (obs - exp) ** 2 / exp for obs, exp in zip(observed, expected)
        )
        return chi_square_statistic
    
    def shift_array_right(self,arr,n=1):
        if not arr or n <= 0:
            return arr  
        n %= len(arr) 
        for _ in range(n):
            last_element = arr.pop()
            arr.insert(0, last_element)
        return arr
    
    def breakCipher(self):
        frequencies = self.calcFreq()
        observed = [frequencies[letter] for letter in "abcdefghijklmnopqrstuvwxyz"]

        chiSqArr = []
        for i in range(26):
            currentArr = self.shift_array_right(observed, i)
            chiRes = self.getChi(currentArr, self.normalFreq)
            chiSqArr.append(chiRes)

        # Use np.argmin to find the index of the minimum chi-square value
        best_shift = np.argmin(np.array(chiSqArr))
        return best_shift
    
