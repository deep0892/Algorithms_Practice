# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        next = None
        prev = None
        
        while(current is not None):
            next = current.next
            current.next = prev 
            prev = current
            current = next
        head = prev 
            
        return head


def main():
    head = [1,2,3,4,5]
    sol = Solution()
    print(sol.reverseList(head))


if __name__ == "__main__":
    main()


