# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
"""
Discription of question in above link
Given a 6*6 2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
a b c
  d
e f g
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6*6.
"""

from typing import List


class Solution:
    def hourglassSum(self, arr):
        arr_sum = []
        
        for i in range(1, len(arr)-1, 1):
            sum = 0
            for j in range(1, len(arr)-1, 1):
                sum = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
                arr_sum.append(sum)
        
        max_sum = arr_sum[0]
        for el in arr_sum:
            if max_sum < el:
                max_sum = el
                
        return max_sum


def main():
    queries = [[1, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0],
              [0, 0, 2, 4, 4, 0],
              [0, 0, 0, 2, 0, 0],
              [0, 0, 1, 2, 4, 0]]
    sol = Solution()
    print(sol.hourglassSum(queries))


if __name__ == "__main__":
    main()
