# https://leetcode.com/problems/longest-palindromic-substring/
"""
Discription of question in above link
"""

from typing import List
import math

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) < 1 or s == None): return ''
        
        start: int = 0
        end: int = 0

        for i in range(0, len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i + 1)
            length = max(len1, len2)

            if (length > end - start):
                start = i - int((length - 1) / 2)
                end = i + int(length / 2)
        return s[start:end + 1]

    def expandFromMiddle(self, s: str, left: int, right: int) -> int:
        if (s == None or left > right): return 0
            
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            
        return right - left - 1
                


def main():
    n = "babad"
    sol = Solution()
    print(sol.longestPalindrome(n))
    n = "cbbd"
    print(sol.longestPalindrome(n))
    n = "abcabcabcabc"
    print(sol.longestPalindrome(n))


if __name__ == "__main__":
    main()
