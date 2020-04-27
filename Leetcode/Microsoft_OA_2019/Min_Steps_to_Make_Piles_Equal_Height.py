# https://leetcode.com/discuss/interview-question/364618/
"""
Discription of question in above link
"""
from typing import List

def min_step(arr: List[int]) -> int:
    if len(arr) <= 1:
        return 0
    res: int = 0
    distint_nums: int = 0
    arr.sort()

    for i in range(1, len(arr)):
        if(arr[i] == arr[i-1]):
            res += distint_nums
        else:
            distint_nums +=1
            res += distint_nums

    return res

# Driver program to test the above function
def main(): 
    tests = [
        [1, 2, 2, 2, 3, 4, 5, 6, 4, 12, 4],
        [3, 2, 1],
        [1, 2, 5],
        [1, 2, 3, 4, 5]
    ]

    for t in tests:
        print(min_step(t))

if __name__=="__main__": 
    main()
