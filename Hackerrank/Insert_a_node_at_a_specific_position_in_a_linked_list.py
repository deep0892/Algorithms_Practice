# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming
"""
You can perform the following operations on the string, :
1.Capitalize zero or more of 's lowercase letters.
2.Delete all of the remaining lowercase letters in .
Given two strings, a and b, determine if it's possible to make  equal to  as described. 
If so, print YES on a new line. Otherwise, print NO.
"""

from typing import List


# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(head, data, position):
    print(data, position)
    if head is None:
        return SinglyLinkedListNode(data)
    
    start = head
    for i in range(position-1):
        start = start.next
    
    new_node = SinglyLinkedListNode(data)
    temp = start.next
    start.next = new_node
    new_node.next= temp
        
    return head


def main():
    a = 'daBcd'
    b = 'ABC'
    sol = Solution()


if __name__ == "__main__":
    main()
