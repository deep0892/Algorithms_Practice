# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""
Discription of question in above link
"""

from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result: str = ''
        stringBuilder = ''
        cnt_o: int = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt_o += 1
            elif s[i] == ')':
                if cnt_o == 0:
                    continue
                cnt_o -=1
            stringBuilder += s[i]
        print(cnt_o)
        print(stringBuilder)
        for j in range(len(stringBuilder)-1, -1, -1):
            if stringBuilder[j] == "(": 
                if cnt_o > 0:
                    cnt_o -= 1 
                    continue
            result += stringBuilder[j]
            
        return result[-1::-1]

def main():
    s = "lee(t(c)o)de)"
    sol = Solution()
    print(sol.minRemoveToMakeValid(s))
    s = "a)b(c)d"
    print(sol.minRemoveToMakeValid(s))
    s =  "))(("
    print(sol.minRemoveToMakeValid(s))
    s =  "(a(b(c)d)"
    print(sol.minRemoveToMakeValid(s))

if __name__ == "__main__":
    main()
