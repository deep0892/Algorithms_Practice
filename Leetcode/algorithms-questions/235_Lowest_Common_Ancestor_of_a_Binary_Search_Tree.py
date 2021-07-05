# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if(p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root


def main():
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node8 = TreeNode(8)
    node6.left = node2
    node6.right = node8
    node0 = TreeNode(0)
    node4 = TreeNode(4)
    node2.left = node0
    node2.right = node4
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node8.left = node7
    node8.right = node9
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node4.right = node5
    node4.left = node3
    sol = Solution()
    print(sol.findMode(node6, node2, node8))


if __name__ == "__main__":
    main()
