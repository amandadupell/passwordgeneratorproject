#!/usr/local/bin/python3

import argparse
import random

wordlist = open("wordlist.txt", "r").readlines()

parser = argparse.ArgumentParser("Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w", "--words", type=int, default=4, help="include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", type=int, default=0,
                    help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", type=int, default=0,
                    help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", type=int, default=0,
                    help="insert SYMBOLS random symbols in the password (default=0)")

args = parser.parse_args()
numWords = args.words
numCaps = args.caps
numNums = args.numbers
numSyms = args.symbols
password = []
output = ""
x = 0
y = 0
z = 0
s = 0

while x < numWords:
    randomWord = wordlist[random.randint(0, len(wordlist) - 1)]
    password.append(randomWord)
    x += 1

cappedIndex = []
while y < numCaps:
    randomInt = random.randint(0, len(password) - 1)
    capitalize = password[randomInt]
    if randomInt in cappedIndex:
        continue
    cappedIndex.append(randomInt)
    begin = capitalize[:1]
    end = capitalize[1:]
    capitalizedWord = begin.upper() + end
    password.remove(capitalize)
    password.insert(randomInt, capitalizedWord)
    y += 1

while z < numNums:
    insertNum = str(random.randint(0, 9))
    insertAt = random.randint(0, len(password))
    if insertAt is 0:
        password.insert(0, insertNum)
    else:
        password.insert(insertAt, insertNum)
    z += 1

symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]
while s < numSyms:
    insertSym = symbols[random.randint(0, len(symbols) - 1)]
    insertAt = random.randint(0, len(password))
    if insertAt is 0:
        password.insert(0, insertSym)
    else:
        password.insert(insertAt, insertSym)
    s += 1

for x in range(0, len(password)):
    output += password[x].strip('\n')

print(output)
