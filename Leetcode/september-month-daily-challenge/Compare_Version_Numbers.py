# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3454/

"""
Problem Statement:

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
"""

## Solution:
from functools import reduce
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1,arr2 = list(map(lambda x: int(x),version1.split('.'))),list(map(lambda x: int(x),version2.split('.')))
        i = 0
        greater = len(arr1) > len(arr2)
        a,b = len(arr1), len(arr2)
        min_arr = min(a, b)
        while ( i < min_arr):
            if( arr1[i] == arr2[i]):
                i += 1
            elif (arr1[i] > arr2[i]):
                return 1
            else:
                return -1
        
        s = reduce(lambda x, y: (x + y) , arr1[i:] if greater else arr2[i:] if a < b else [0])  
        
        return 1 if greater and s != 0 else - 1 if (len(arr1) < len(arr2)) and s != 0 else 0

def main():
    sol = Solution()
    version1 = "0.1"
    version2 = "1.1"
    print(sol.compareVersion(version1, version2))
    version1 = "1.0.1"
    version2 = "1"
    print(sol.compareVersion(version1, version2))
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    print(sol.compareVersion(version1, version2))
    version1 = "1.01"
    version2 = "1.001"
    print(sol.compareVersion(version1, version2))
    version1 = "1.0"
    version2 = "1.0.0"
    print(sol.compareVersion(version1, version2))


if __name__ == "__main__":
    main()