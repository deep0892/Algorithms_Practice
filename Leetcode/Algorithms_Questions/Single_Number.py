# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)


def main():
    nums = [2,2,1]
    sol = Solution()
    print(sol.singleNumber(nums))


if __name__ == "__main__":
    main()


