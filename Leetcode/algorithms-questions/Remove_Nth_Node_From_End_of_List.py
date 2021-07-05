# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head
        for i in range(n):
            if(second.next == None):
                if(i == n - 1):
                    head = head.next
                return head
            second = second.next
          
        while(second.next != None):
            second = second.next
            first = first.next
            
        first.next = first.next.next
        
        return head


def main():
    head = [1, 2, 3, 4, 5]
    n = 2
    sol = Solution()


if __name__ == "__main__":
    main()



