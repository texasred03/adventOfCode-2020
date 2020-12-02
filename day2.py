#!/usr/bin/python3

textFile = open(r"day2.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

''' 
        Sample input
 1-3 a: abcde
 1-3 b: cdefg
 2-9 c: ccccccccc

        Part 1
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times 
 
        Part 2
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on.
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
'''
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
    if letterCount >= minimum and letterCount <= maximum:
        part1Total += 1
    # part 2
    if (password.startswith(letter, minimum-1) or password.startswith(letter, maximum-1)) and not (password.startswith(letter, minimum-1) and password.startswith(letter, maximum-1)):
        part2Total += 1

print(part1Total)
print(part2Total)