# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/

"""
Problem Statement: 
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

"""


# Solution:
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dict = {}
        keyword = set()
        arr = str.split(" ")
        str_arr = list(pattern)
        flag = 1
        if(len(arr) != len(str_arr)):
            return False
        for i in range(len(str_arr)):
            if( not dict.__contains__(str_arr[i]) and arr[i] not in keyword ):
                dict[str_arr[i]] = arr[i]
                keyword.add(arr[i])
            elif(not dict.__contains__(str_arr[i]) and arr[i] in keyword  ):
                flag = 0;
                break;
            else:
                if( dict[str_arr[i]] != arr[i] ):
                    flag = 0;
                    break;
        return flag == 1

def main():
    sol = Solution()
    pattern = "abba"
    str = "dog cat cat dog"
    print(sol.wordPattern(pattern, str))
    pattern = "abba"
    str = "dog cat cat fish"
    print(sol.wordPattern(pattern, str))
    pattern = "aaaa"
    str = "dog cat cat dog"
    print(sol.wordPattern(pattern, str))
    pattern = "abba"
    str = "dog dog dog dog"
    print(sol.wordPattern(pattern, str))


if __name__ == "__main__":
    main()