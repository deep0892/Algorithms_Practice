# https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""
Discription of question in above link
"""

from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev: int = None
    count: int = 1
    max: int = 0

    def findMode(self, root: TreeNode) -> List[int]:
        modes = []
        self.traverse(root, modes)
        return modes

    def traverse(self, node: TreeNode, modes: List[int]) -> None:
        if(node == None):
            return True
        self.traverse(node.left, modes)

        if(self.prev != None):
            if(self.prev == node.val):
                self.count += 1
            else:
                self.count = 1

        if(self.count > self.max):
            self.max = self.count
            modes.clear()
            modes.append(node.val)
        elif(self.count == self.max):
            modes.append(node.val)

        self.prev = node.val
        self.traverse(node.right, modes)


def main():
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.right = None
    root.right.left = TreeNode(2)
    sol = Solution()
    print(sol.findMode(root))


if __name__ == "__main__":
    main()
