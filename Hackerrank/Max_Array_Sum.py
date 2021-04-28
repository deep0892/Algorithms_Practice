# https://www.hackerrank.com/challenges/max-array-sum/copy-from/195747173?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. 
Calculate the sum of that subset. 
It is possible that the maximum sum is , the case when all elements are negative.
"""

from typing import List

class Solution:
    def maxSubsetSum(self, arr):
        inc = arr[0]
        exc = 0
        
        for i in range(1,len(arr)):
            new_excl = exc if exc > inc else inc 
            
            inc = exc + arr[i]
            exc = new_excl  
        return exc if exc > inc else inc


def main():
    queries = [3, 7, 4, 6, 5]
    sol = Solution()
    print(sol.maxSubsetSum(queries))


if __name__ == "__main__":
    main()
