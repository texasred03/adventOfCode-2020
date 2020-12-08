#!/usr/bin/python3
import re

textFile = open(r"day4.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

def isPassportValid(passport):
    passportFields = passport.split()
    
    reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    if len(passportFields) <= len(reqFields):
        if "cid" in passport or len(passportFields) < len(reqFields):
            return False # Satisfies part 1
       
    for field in passportFields:
        fieldType = field.split(":")[0]
        data = field.split(":")[1]
        
        if fieldType == 'byr' and not re.match("(19[2-8][0-9]|199[0-9]|200[0-2])", data): 
            return False
        elif fieldType == 'iyr' and not re.match("(201[0-9]|2020)", data):
            return False
        elif fieldType == 'eyr' and not re.match("(202[0-9]|2030)", data):
            return False
        elif fieldType == 'hgt':
            if not re.match("(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in", data):
                return False
        elif fieldType == 'hcl' and not re.match("#[a-f0-9]{6}", data):
            return False
        elif fieldType == 'ecl' and not re.match("amb|blu|brn|gry|grn|hzl|oth", data):
            return False
        elif fieldType == 'pid' and not re.match("^\d{9}$", data):
            return False
    return True

i = 0
numValidPassports = 0
while i < len(fileData)-1:
    passport = ""
    while i < len(fileData) and fileData[i] != "":
        passport += fileData[i] + " "
        i += 1
    if isPassportValid(passport):
        numValidPassports += 1
    i += 1

print("Valid passports: " + str(numValidPassports))
