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
