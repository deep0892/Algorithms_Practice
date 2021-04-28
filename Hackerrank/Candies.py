# https://www.hackerrank.com/challenges/candies/copy-from/210827439?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
"""
Alice is a kindergarten teacher. 
She wants to give some candies to the children in her class.  
All the children sit in a line and each of them has a rating score according to his or her performance in the class.  
Alice wants to give at least 1 candy to each child. 
If two children sit next to each other, then the one with the higher rating must get more candies. 
Alice wants to minimize the total number of candies she must buy.
"""

from typing import List


class Solution:
    def candies(self, n, arr):
        k = n
        candy = [1 for j in range(0, n + 1)]
        ratings = arr
        ratings.append(0)
        for i in range(1, k):
            c = candy[i]
            left = ratings[i - 1]
            mid = ratings[i]
            right = ratings[i + 1]

            if left < mid <= right:
                c = candy[i - 1] + 1
            elif left < mid and mid > right:
                c = candy[i - 1] + 1
            elif left > mid:
                j = i
                while i > 0 and ratings[j - 1] > ratings[j]:
                    candy[j - 1] = max(candy[j - 1], candy[j] + 1)
                    j -= 1
            elif left == mid or mid == right:
                c = 1

            candy[i] = c
        return sum(candy)-1


def main():
    arr=[4,6,4,5,6,2]
    sol = Solution()
    print(sol.candies(len(arr),arr))


if __name__ == "__main__":
    main()
