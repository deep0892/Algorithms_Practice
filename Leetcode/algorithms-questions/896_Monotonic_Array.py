# https://leetcode.com/problems/monotonic-array/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing: boolean = True
        decreasing: boolean = True

        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing


def main():
    A = [1, 2, 2, 3]
    sol = Solution()
    print(sol.isMonotonic(A))
    A = [6, 5, 4, 4]
    print(sol.isMonotonic(A))
    A = [1, 3, 2]
    print(sol.isMonotonic(A))
    A = [1, 2, 4, 5]
    print(sol.isMonotonic(A))
    A = [1, 1, 1]
    print(sol.isMonotonic(A))


if __name__ == "__main__":
    main()
