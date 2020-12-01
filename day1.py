#!/usr/bin/python3

textFile = open(r"day1.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

# find the two entries that sum to 2020 and then multiply those two numbers together.
def part1():
    for currentNumber in fileData:
        numToFind = 2020 - int(currentNumber)
        if str(numToFind) in fileData:
            return numToFind * int(currentNumber)

# find three numbers in your expense report that meet the same criteria
def part2():
    for x in fileData:
        for y in fileData:
            numToFind = 2020 - (int(x) + int(y))
            if str(numToFind) in fileData:
                return int(x) * int(y) * numToFind

print(part1())
print(part2())
