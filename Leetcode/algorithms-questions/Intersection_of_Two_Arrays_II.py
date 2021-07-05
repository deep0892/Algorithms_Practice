# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_1 = {}
        intersection_arr = []
        for item in nums1:
            dict_1[item] = dict_1.get(item,0) + 1
        
        for el in nums2:
            if dict_1.get(el,0) > 0:
                intersection_arr.append(el)
                dict_1[el] = dict_1.get(el,0) - 1
            
        return intersection_arr


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2,2]
    sol = Solution()
    print(sol.intersect(nums1, nums2))


if __name__ == "__main__":
    main()
