#!/usr/bin/python3
import numpy as np

textFile = open(r"day6.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

# Part 1
i = 0
total = 0
while i < len(fileData):
    questions = []
    while i < len(fileData) and fileData[i] != "":
        for char in fileData[i]:
            questions.append(char)
        i += 1
    total += len(np.unique(np.array(questions)))
    i += 1
print(total)