# https://leetcode.com/problems/house-robber/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result: int = 0
        dp = [0] * (len(nums)+1)

        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], dp[i-1]+nums[i])

        return dp[len(nums)]


def main():
    nums = [1, 2, 3, 1]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    main()
