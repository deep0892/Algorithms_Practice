# https://leetcode.com/problems/generate-parentheses/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result

    def backtrack(
            self,
            result: List[str],
            current_string: str,
            open: int,
            close: int,
            max: int):
        print
        if len(current_string) == max * 2:
            result.append(current_string)
            return
        if(open < max):
            self.backtrack(result, current_string + '(', open + 1, close, max)
        if(close < open):
            self.backtrack(result, current_string + ')', open, close + 1, max)


def main():
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))


if __name__ == "__main__":
    main()
