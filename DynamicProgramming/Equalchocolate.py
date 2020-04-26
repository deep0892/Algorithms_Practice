# https://www.hackerrank.com/challenges/equal/problem

"""
Christy is interning at HackerRank. 
One day she has to distribute some chocolates to her colleagues. 
She is biased towards her friends and plans to give them more than the others. 
One of the program managers hears of this and tells her to make sure everyone gets the same number.
To make things difficult, she must equalize the number of chocolates in a series of operations. 
For each operation, she can give 1,2 or 5 chocolates to all but one colleague. 
Everyone who gets chocolate in a round receives the same number of pieces.
For example, assume the starting distribution is [1,1,5]. 
She can give  bars to the first two and the distribution will be [3,3,5]. 
On the next round, she gives the same two  bars each, and everyone has the same number: [5,5,5].
Given a starting distribution, 
calculate the minimum number of operations needed so that every colleague has the same number of chocolates.
"""

import sys

def count(arr):
    arr.sort()
    sum = sys.maxsize
    for base in range(0,3):
        current_sum = 0
        for i in range(0,len(arr)):
            delta = arr[i] - arr[0] + base
            current_sum += int(delta/5) +  int( (delta % 5) /2) + delta % 5 % 2
        sum = min(sum,current_sum)
    return sum
    
    
# Driver program to test the above function
def main(): 
    arr =  [1,1,5]
    m = len(arr)
    print(count(arr))
  
if __name__=="__main__": 
    main()
