#!/usr/bin/python3

textFile = open(r"day5.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

def getSeatId(data):
    binaryData = data.translate(data.maketrans('BRFL','1100')) # Converts characters in string: B/R to 1 and F/L to 0. 
    row = int(binaryData[0:7],2) # int(number, base) converts a number from specified base. In this example it will convert from binary (base 2)
    column = int(binaryData[7:10], 2)  
    return row * 8 + column

seatIds = []
for inputData in fileData:
    seatIds.append(getSeatId(inputData))
    
print("Highest seat ID: " + str(max(seatIds)))

i = 0
mySeat = 0
while i < len(seatIds):
    if i not in seatIds and (i-1 in seatIds and i+1 in seatIds):
        mySeat = i
        break
    i+=1
    
print("My seat ID: " + str(mySeat))