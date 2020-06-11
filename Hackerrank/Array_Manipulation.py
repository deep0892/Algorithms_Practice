# https://www.hackerrank.com/challenges/crush/problem
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def arrayManipulation(self, n, queries):
        arr = [0] * (n+1)
        max_v = 0
        x = 0
        for querie in queries:
            a, b, k = querie[0], querie[1], querie[2]
            arr[a-1] += k
            if b < n:
                arr[b] -= k
        for i in range(n):
            x += arr[i]
            if max_v < x:
                max_v = x
        return max_v


def main():
    n = 5
    queries = [[1, 2, 100],
               [2, 5, 100],
               [3, 4, 100]]
    sol = Solution()
    print(sol.arrayManipulation(n, queries))


if __name__ == "__main__":
    main()
