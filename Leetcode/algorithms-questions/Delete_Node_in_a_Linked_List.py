# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while(node.next is not None):
            temp = node
            node.val = node.next.val
            node.next.val = temp.val
            node = node.next
        temp.next = None
        return


def main():
    head = [4, 5, 1, 9]
    node = 5
    sol = Solution()


if __name__ == "__main__":
    main()


