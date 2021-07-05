# https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/569/
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        steps = [0 for i in range(n)]
        steps[0] = 1
        steps[1] = 2
        
        if n<=2:
            return steps[n-1]
        
        for i in range(2,n):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n-1]


def main():
    n = 5
    sol = Solution()
    print(sol.climbStairs(n))


if __name__ == "__main__":
    main()
