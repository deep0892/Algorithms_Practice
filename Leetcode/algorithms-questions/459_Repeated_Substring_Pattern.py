# https://leetcode.com/problems/repeated-substring-pattern/
"""
Discription of question in above link
"""

from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(length - 1, 0, -1):
            if (length % i == 0):
                num_repeats = int(length / i)
                substring = s[0:i]
                sb = ''
                for j in range(0, num_repeats):
                    sb += substring
                if sb == s: return True
        return False

def main():
    n = "abab"
    sol = Solution()
    print(sol.repeatedSubstringPattern(n))
    n = "aba"
    print(sol.repeatedSubstringPattern(n))
    n = "abcabcabcabc"
    print(sol.repeatedSubstringPattern(n))


if __name__ == "__main__":
    main()
