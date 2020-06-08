# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""
Discription of question in above link
"""

from typing import List
import sys
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
       result: int = 0
       if len(nums) == 0 or len(nums) == 1:
         return 0
       max_num:int = -sys.maxsize
       min_num: int = sys.maxsize
       
       flag: boolean = False
       
       for i in range(1, len(nums)):
         if nums[i] < nums[i-1]:
          flag = True
         if flag:
           min_num = min(nums[i],min_num)
           
       flag = False
       for i in range(len(nums)-2, -1, -1):
         if nums[i] > nums[i+1]:
          flag = True
         if flag:
           max_num = max(nums[i],max_num)
           
       for l in range(0, len(nums)):
         if(min_num < nums[l]):
           break
         
       for r in range(len(nums)-1, -1, -1):
         if(max_num > nums[r]):
           break
       print(max_num, min_num, r, l)
       if(r-l < 0): 
          return 0
       else:
          return r - l + 1
        
        
def main():
    A = [2, 6, 4, 8, 10, 9, 15]
    sol = Solution()
    print(sol.findUnsortedSubarray(A))
    
if __name__ == "__main__":
    main()
