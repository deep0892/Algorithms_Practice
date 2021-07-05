# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if(matrix == None or len(matrix) == 1): return
        n = len(matrix)
        for i in range(0, n//2 + 1):
            for j in range(i, n-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
                
        return


def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    sol.rotate(matrix)
    print(matrix)


if __name__ == "__main__":
    main()



