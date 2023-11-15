import math
letter_frequencies = {
    'a': 8.11,
    'b': 1.84,
    'c': 2.33,
    'd': 4.18,
    'e': 10.57,
    'f': 1.84,
    'g': 2.46,
    'h': 6.63,
    'i': 6.88,
    'j': 0.12,
    'k': 0.61,
    'l': 4.18,
    'm': 1.35,
    'n': 8.48,
    'o': 8.48,
    'p': 1.60,
    'q': 0.00,
    'r': 5.77,
    's': 6.14,
    't': 8.23,
    'u': 2.21,
    'v': 2.09,
    'w': 3.81,
    'x': 0.00,
    'y': 2.09,
    'z': 0.00
}

top_5_letters = {
    'e': 10.57,
    'n': 8.48,
    'o': 8.48,
    't': 8.23,
    'a': 8.11
}

printArray = []
alpha = list(letter_frequencies.keys())
for i in alpha:
    printArray.append([" "]*len(alpha)*3)

for i in range(len(alpha)*3):
    if i % 3 == 0:
        printArray[-1][i] = alpha[int(i/3)].capitalize()
    if i != len(alpha)*3 - 1:
        printArray[-2][i] = "_"

for i in range(len(printArray) - 1):
    if i != len(printArray) - 2:
        printArray[i][-1] = f"| {alpha[i].capitalize()}- {letter_frequencies[alpha[i]]}%"
    else:
        printArray[i][-1] = "|"

sideArray = ["TOP 5 FREQ", "----------"] + [f"| {i.capitalize()}- {top_5_letters[i]} %" for i in top_5_letters.keys()]

for i in range(11,18):
    printArray[i].append("\t\t"+sideArray[i-11])

starArr = []
for i in alpha:
    starArr.append(math.ceil((letter_frequencies[i])/100*26))


for i,v in enumerate(starArr):
    verticalIndex = i * 3
    for i in range(v):
        printArray[23-i][verticalIndex] = "*"

# print everything
[print("".join(i)) for i in printArray]

#for i in printArray:
#    print("".join(i))

"""
sideArray = ["TOP 5 FREQ","----------"]
topfreqs = [f"| {i.capitalize()}- {top_5_letters[i]}%" for i in top_5_letters.keys()]
sideArray = sideArray + topfreqs
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphString = "  ".join([letter.capitalize() for letter in alphabet])

startPrinting = False
sidePrinterNum = 0
for i in alphabet:
    if i == "k":
        startPrinting = True
    if i == "r" or sidePrinterNum > len(sideArray):
        startPrinting = False
    sideStr = ""
    if startPrinting:
        sideStr = sideArray[sidePrinterNum]
        sidePrinterNum += 1
    print(len(alphString)*" " + f" | {i.capitalize()}- {letter_frequencies[i]}%" + "\t\t" + sideStr)
print(len(alphString)*"_" + "_|")
print(alphString)


print("TOP 5 FREQ")
print("----------")
for i in top_5_letters.keys():
    print(f"| {i.capitalize()}- {top_5_letters[i]}%")

    """