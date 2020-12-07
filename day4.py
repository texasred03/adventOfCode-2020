
#!/usr/bin/python3

textFile = open(r"day4.txt", 'r')
fileData = textFile.read().splitlines()
textFile.close()

def isPassportValid(passport):
    reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    print(passport)

    passportFields = passport.split(" ")
    if len(passportFields) <= 7 and "cid" in passport:
        return False
    #for field in passportFields:
    #    if field.split(":")[0] not in reqFields:
            
            
    print("valid!")
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

print(numValidPassports)