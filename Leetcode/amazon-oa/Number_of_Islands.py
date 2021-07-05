# https://leetcode.com/problems/number-of-islands/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        noOfIslands = 0
        rows = len(grid)
        columns = len(grid[0])

        visited = [[False for i in range(columns)] for j in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and visited[i][j] == False:
                    self.dfs(grid, i, j, rows, columns, visited)
                    noOfIslands += 1

        return noOfIslands

    def dfs(self, grid, i, j, rows, columns, visited):
        if(i < 0 or j < 0 or i >= rows or j >= columns or grid[i][j] == 0 or visited[i][j]):
            return

        visited[i][j] = 1
        self.dfs(grid, i+1, j, rows, columns, visited)
        self.dfs(grid, i-1, j, rows, columns, visited)
        self.dfs(grid, i, j+1, rows, columns, visited)
        self.dfs(grid, i, j-1, rows, columns, visited)


def main():
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    sol = Solution()
    print(sol.numIslands(grid))


if __name__ == "__main__":
    main()
