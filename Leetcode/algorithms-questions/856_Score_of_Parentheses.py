# https://leetcode.com/problems/score-of-parentheses/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        score = 0
        for el in S:
            if el == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score*2, 1)
        return score


def main():
    S = "(()(()))"
    sol = Solution()
    print(sol.scoreOfParentheses(S))


if __name__ == "__main__":
    main()
