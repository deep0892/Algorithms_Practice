# https://www.hackerrank.com/challenges/max-array-sum/copy-from/195747173?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
"""
Two strings are anagrams of each other if the letters of one string can be rearranged to 
form the other string. Given a string, find the number of pairs of substrings of the 
string that are anagrams of each other.
"""

from typing import List

class Solution:
    def sherlockAndAnagrams(self, s):
        # Write your code here
        n = len(s)
        res = 0
        for l in range(1, n):
            cnt = {}
            for i in range(n - l + 1):
                subs = list(s[i:i + l])
                subs.sort()
                subs = ''.join(subs)
                if subs in cnt:
                    cnt[subs] += 1
                else:
                    cnt[subs] = 1
                res += cnt[subs] - 1
                
        return res


def main():
    queries = 'abba'
    sol = Solution()
    print(sol.sherlockAndAnagrams(queries))


if __name__ == "__main__":
    main()
