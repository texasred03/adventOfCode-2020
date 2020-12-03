#!/usr/bin/python3

textFile = open(r"day3.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

def getTreeCount(x, y):
    trees = 0
    column = 1
    for i in range(1, int(len(fileData) / y)):
        line = fileData[i * y]
        column = (column + x) % len(line)
        if line.startswith('#', column-1):
            trees += 1
    return trees

print("Part1: " + str(getTreeCount(3,1)))

paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]

trees = 1
for i in range(0, len(paths)):
    trees *= getTreeCount(paths[i][0], paths[i][1])
print("Part2: " + str(trees))
