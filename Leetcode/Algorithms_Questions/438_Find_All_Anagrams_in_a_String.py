# https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
Discription of question in above link
"""

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result: List = []
        char_map = [0] * 26
        for el in p:
            char_map[ord(el)-ord('a')] += 1
        
        left: int = 0;
        right: int = 0
        count: int = len(p)
        
        while(right < len(s)):
            if(char_map[ord(s[right]) - ord('a')] >= 1):
                count -= 1
            char_map[ord(s[right]) - ord('a')] -= 1
            if(count == 0):
                result.append(left)
                
            if right - left == len(p)-1:
                if(char_map[ord(s[left])-ord('a')] >= 0):
                    count += 1 
                char_map[ord(s[left])-ord('a')] += 1
                left += 1
            right += 1
        return result


def main():
    s = "abab" 
    p = "ab"
    sol = Solution()
    print(sol.findAnagrams(s,p))


if __name__ == "__main__":
    main()
