# Pair shift numbers

The pair shift concept is to have an array of numbers where a given number is only present twice in the array(as in pair) 
and the distance between them being the value of the number.
For example: if the number is 3 then in the array : [....3,x,x,x,3...]. Thus the distance between the two 3s is 3.

The program expects a number and generates a pair shift array where all the values in the array behaves the above property.

One example of pair shift array:
n = 3 means all the values in the array is between 1-3
Two solutions possible:
[3, 1, 2, 1, 3, 2]
[2, 3, 1, 2, 1, 3]

## Constraints

1<=n<=100

## Input

You read the value n from user.

## Output

Aleast one solution if one exists.

## Sample Case 1

3

3 1 2 1 3 2

## Sample Case 2

2

No solution

## Sample Case 3

4
4 1 3 1 2 4 3 2

## Sample Case 4

20 

20 18 19 15 11 17 10 16 9 5 14 1 13 1 12 5 11 10 9 15 18 20 19 17 16 14 13 12 8 4 7 3 6 2 4 3 2 8 7 6

## Sample Case 5

1

No Solution

### Explantion

For sample case 1:

n = 2 means array size is 4 and you only pair of 2 numbers 1,1,2,2. You cannot arrange them in a way the distance between the pairs is always the value. Distance between pair of 2s needs to be 2 which means the pair of 2s can only be at the start and end of the array which leaves the middle spots for pair of 1s but, 1s needs to 1 distance apart as in there needs to be another number in between the 1s

Same goes for n=1

n=3. explanation is well defined in the description.

## Requirement
Any programming language can be used.
Makefile and readme needs to be included for the execution of the program. 
The solution needs to be scalable for any number of values of n for the given range.
