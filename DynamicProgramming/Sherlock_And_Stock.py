# https://www.hackerrank.com/challenges/sherlock-and-cost/problem
"""
In this challenge, you will be given an array B and must determine an array A. 
There is a special rule: 
For all i, A[i] <= B[i]. That is, A[i] can be any number you choose such that 1 <= A[i] <= B[i]. 
Your task is to select a series of A[i] given B[i] such that the sum of the absolute difference of consecutive pairs 
of A[i] is maximized.
"""

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
