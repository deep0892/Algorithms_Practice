# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if hash_map.get(diff,-1) == -1:
                hash_map[nums[i]] = i
            else:
                break
                                
        return [i, hash_map[diff]]


def main():
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))


if __name__ == "__main__":
    main()


