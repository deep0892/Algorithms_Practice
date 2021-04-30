# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        
        while(count < len(nums)):
            nums[count] = 0
            count += 1
        return


def main():
    nums = [0,1,0,3,12]
    sol = Solution()
    print(sol.moveZeroes(nums))


if __name__ == "__main__":
    main()



