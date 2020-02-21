#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  because: the while loop is executed 'n' times
    a = 0                   O(1)
    while (a < n * n * n):  O(n)
      a = a + n * n         O(1)
    
    


b) O(nlogn) because: "while" is a inner loop executed n/2 times and an increment inside multiplying j by 2 that means j increments exponentially and also "while" is into of a "for" loop that is executed n times too. For this reason we have n * logn 
    sum = 0                 O(1)
    for i in range(n):      O(n) iterate n times
      j = 1                 O(1)
      while j < n:          O(n/2) 
        j *= 2              O(1)
        sum += 1            O(1)

I calculate the output of the function vs the calculus of nlogn and its almost similar
n   sum  n logn 
0   0       0           
1   0       0
2   2       2
7   21      19.61
8   24      24
30  150     147.20


c) O(n) because the recursion in this function is based on the amount of bunnies and increment  by 2 in each recursion that means that is linear
   def bunnyEars(bunnies):              # bunnies is a constant
      if bunnies == 0:                  O(1)
        return 0                        O(1)

      return 2 + bunnyEars(bunnies-1)   O(n)

## Exercise II
I would use a binary search: Complexity time O(log n).

First of all, all the building floors  are sorted by definition and also we know that the difference between one floor and the next one is always 1. 

Second, the binary search works in the following way:
We need to find the middle floor of our building using the formula: middle is equals to n//2, we are going to call this floor our 'current floor'
Then we are going to drop an egg from the current floor:
    If the egg is broken we have to calculate the middle floor again between the current floor and the first floor, and this is going to be our new current floor.

    Otherwise, we have to calculate the middle floor between the current floor and the top floor of the building, and this is going to be our new current floor
We need to continue this process until the egg is NOT broken in the current floor but when the egg is broken in the next floor (current floor plus 1) of our current floor.
At the end the output of our function the current floor.
    


