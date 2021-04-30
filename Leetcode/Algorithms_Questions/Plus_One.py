# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry 
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            
        if carry:
            digits.insert(0, 1)
        
        return digits


def main():
    digits = [1,2,3]
    sol = Solution()
    print(sol.plusOne(digits))
    digits = [4, 3, 2, 1]
    print(sol.plusOne(digits))


if __name__ == "__main__":
    main()


