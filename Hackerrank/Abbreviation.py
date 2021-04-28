# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming
"""
You can perform the following operations on the string, :
1.Capitalize zero or more of 's lowercase letters.
2.Delete all of the remaining lowercase letters in .
Given two strings, a and b, determine if it's possible to make  equal to  as described. 
If so, print YES on a new line. Otherwise, print NO.
"""

from typing import List


class Solution:
    def abbreviation(self, a, b):
        isValid = [[ False for i in range(len(b)+1)] for i in range(len(a)+1)]
        isValid[0][0] = True
        for i in range(1, len(a)+1):
            if a[i-1].isupper():
                isValid[i][0] = False;
            else:
                isValid[i][0] = True;   
        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                if a[i-1] == b[j-1]:
                    isValid[i][j] = isValid[i-1][j-1]
                elif a[i-1].upper() == b[j-1]:
                    isValid[i][j] = isValid[i-1][j-1] or isValid[i-1][j]
                elif a[i-1].isupper():
                    isValid[i][j] = False
                else:
                    isValid[i][j] = isValid[i-1][j]
        return "YES" if isValid[len(a)][len(b)] else "NO"


def main():
    a = 'daBcd'
    b = 'ABC'
    sol = Solution()
    print(sol.abbreviation(a, b))


if __name__ == "__main__":
    main()
