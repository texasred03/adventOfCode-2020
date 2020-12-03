#!/usr/bin/python3

textFile = open(r"day2.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

part1Total = 0
part2Total = 0
for line in fileData:
    splitPassword = line.split()
    minimum = int(splitPassword[0].split("-")[0])
    maximum = int(splitPassword[0].split("-")[1])
    letter = splitPassword[1].replace(":","")
    password = splitPassword[2]

    # part 1
    letterCount = password.count(letter)
    if minimum <= letterCount <= maximum:
        part1Total += 1
    # part 2
    if (password.startswith(letter, minimum-1) or password.startswith(letter, maximum-1)) and not (password.startswith(letter, minimum-1) and password.startswith(letter, maximum-1)):
        part2Total += 1

print(part1Total)
print(part2Total)
