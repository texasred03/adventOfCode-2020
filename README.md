# Advent of Code 2020 Challenge

I will be participating in the 2020 Advent of Code challenge that can be found: https://adventofcode.com/ 

Since I am new to python I am trying to not use any third party libraries.  Once the challenge is completed I will give everything a second pass and see how to better utilize those libraries. 

## Day 1
### Part 1
Find the two entries that sum to 2020 and then multiply those two numbers together.
### Part 2
Find three numbers in your expense report that meet the same criteria.
### Sample Input
```1721
979
366
299
675
1456
```
### Thoughts
Part one was pretty simple.  Part two was also pretty simple although I know it's not the most effecient.  

## Day 2
### Part 1
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times 
### Part 2
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on.
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
### Sample Input
``` 
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```
### Thoughts
Both parts were pretty easy.  I ran into an issue when starting part 2, but I had misread the requirements! 

## Day 3
Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. The same pattern repeats to the right many times. You start on the open square (.) in the top-left corner and need to reach the bottom
### Part 1
Count all the trees you would encounter for the slope right 3, down 1.
### Part 2
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom. 
#### Slopes
```
Right 1, down 1.
Right 3, down 1. 
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
```
### Sample Input
```
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```
### Thoughts
The first part was pretty easy.  The second part was a little more challenging due to the increase in down slope.  It just required a little more thinking. 

## Day 4
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines. There are expected fields in the passport:
```
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
```
### Part 1
A passport is valid only when it contains a minimum of seven fields.  CID is the only optional field. 
### Part 2
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
```
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
```
### Sample Input
```
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
```
### Thoughts
This took awhile.  I've come to find out I'm not nearly as knowledgeable about regex as I should be. I also learned that python has no concept of a switch statement, which would have made things a little easier.  This was a fun and frustrating puzzle. 

## Day 5
You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input). A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right". The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

### Part 1
What is the highest seat ID on a boarding pass?
### Part 2
Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
What is the ID of your seat?
### Sample Input
```
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
```
### Thoughts
This was a fun one and I really learned a lot of python, specifically that you can convert a string from a specified base to a decimal.  Once I learned that, this puzzle was pretty easy. 