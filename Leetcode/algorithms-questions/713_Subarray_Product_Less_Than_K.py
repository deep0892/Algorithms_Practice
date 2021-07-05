# https://leetcode.com/problems/subarray-product-less-than-k/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k <= 1):
            return 0
        prod: int = 1
        result: int = 0

        left: int = 0
        right: int = 0

        while(right < len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1

            result += right - left + 1
            right += 1
        return result


def main():
    nums = [10, 5, 2, 6]
    k = 100
    sol = Solution()
    print(sol.numSubarrayProductLessThanK(nums, k))


if __name__ == "__main__":
    main()
