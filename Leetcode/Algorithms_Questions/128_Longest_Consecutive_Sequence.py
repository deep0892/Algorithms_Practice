# https://leetcode.com/problems/longest-consecutive-sequence/
"""
Discription of question in above link
"""

from typing import List

# O(n^3)
class Solution_O_n_3:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence_length = 0
        
        for i in range(len(nums)):
            current_num = nums[i]
            current_sequence_length = 1
            
            while(self.numberExists(nums,current_num+1)):
                current_num += 1
                current_sequence_length +=1
            max_sequence_length = max(max_sequence_length, current_sequence_length)
        
        return max_sequence_length
    
    def numberExists(self, nums, num):
        for i in range(len(nums)):
            if nums[i] == num:
                return True
        return False

# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence_length = 0
        hash = {}
        
        for i in range(len(nums)):
            hash[nums[i]] = 1
        
        for i in range(len(nums)):
            current_num = nums[i]
            current_sequence_length = 1
            
            if not hash.__contains__(current_num - 1):
                while(hash.__contains__(current_num+1)):
                    current_num += 1
                    current_sequence_length += 1
                max_sequence_length = max(max_sequence_length, current_sequence_length)  
        
        return max_sequence_length



def main():
    S = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(S))


if __name__ == "__main__":
    main()
