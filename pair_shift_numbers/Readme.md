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
