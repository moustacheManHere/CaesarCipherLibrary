from Ram.Base.Node import Node
from Ram.Cipher.Caesar import Caesar
from Ram.Base.File import File
from Ram.Stat.Frequency import Frequency
from math import log


class CaeserFile(Node, Caesar, File):
    def __init__(self, filename):
        File.__init__(self, filename)
        Caesar.__init__(self, self.txt)

        self.freq = Frequency(filename)

    def breakCaesar(self, ref):
        expected = ref.getAlphaList()[1]
        frequency = self.freq.getAlphaList()[1]
        rotated_sequences = []
        length = len(frequency)
        for i in range(length):
            rotated_sequence = frequency[i:] + frequency[:i]
            rotated_sequences.append(rotated_sequence)

        scores = []
        for k in rotated_sequences:
            kl = self.kl_divergence(k, expected)
            scores.append(kl)

        self.key = scores.index(min(scores))
        self.decrypt(self.key)

    def kl_divergence(self, p, q):
        if len(p) != len(q):
            print(len(p), len(q))
            print("Error: KL Divergence input distributions must have the same length")
            return None
        epsilon = 1e-10
        divergence = sum(
            p_i * (log(p_i + epsilon) - log(q_i + epsilon)) for p_i, q_i in zip(p, q)
        )
        return divergence

    def getKey(self):
        return self.key
