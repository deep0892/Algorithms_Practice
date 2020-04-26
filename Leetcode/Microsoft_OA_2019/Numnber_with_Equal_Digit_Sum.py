# https://leetcode.com/discuss/interview-question/365872/
"""
Given an array in n integers, return the max sum of 2 integers
whose digits add upto an equal sum. If there are no 2 numbers whose digits have 
an equal sum, the function should return -1
"""
def digit_sum(n):
    sum = 0
    while(n>0):
        sum += n%10
        n //=10
    return sum
    

def count(arr):
    digit_sum_map = {}
    max_sum = -1
    for el in arr:
        dsum = digit_sum(el)
        if dsum in digit_sum_map:
            max_sum = max(max_sum, el+digit_sum_map[dsum])
            digit_sum_map[dsum] = max(digit_sum_map[dsum],el)
        else:
            digit_sum_map[dsum] = el
    return max_sum
    
    
# Driver program to test the above function
def main(): 
    arr =  [51,32,43]
    m = len(arr)
    print(count(arr))
  
if __name__=="__main__": 
    main()
