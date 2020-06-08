# https://leetcode.com/problems/global-and-local-inversions/
"""
Discription of question in above link
"""

from typing import List

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        if(len(A)==0 or len(A) == 1):
          return True
        
        max_num = -1
        for i in range(0, len(A)-2):
          max_num = max(A[i], max_num)
          if(max_num > A[i+2]):
            return False
        return True
        
        
def main():
    A = [1,0,2]
    sol = Solution()
    print(sol.isIdealPermutation(A))
    A = [1,2,0]
    print(sol.isIdealPermutation(A))
    A = [0,1]
    print(sol.isIdealPermutation(A))
if __name__ == "__main__":
    main()
