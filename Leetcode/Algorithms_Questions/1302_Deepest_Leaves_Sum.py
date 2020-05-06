# https://leetcode.com/problems/deepest-leaves-sum/
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
    def deepestLeavesSum(self, root: TreeNode) -> int:

        if(root == None):
            return 0
        if(root.left == None and root.right == None):
            return root.val
        queue = [root]
        level_sum = 0

        while(len(queue) != 0):
            level_sum = 0
            size = len(queue)
            for i in range(0, size):
                current_node = queue.pop(0)
                level_sum += current_node.val
                if(current_node.left != None):
                    queue.append(current_node.left)
                if(current_node.right != None):
                    queue.append(current_node.right)

        return level_sum


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node5 = TreeNode(5)
    node2.right = node5
    sol = Solution()
    print(sol.deepestLeavesSum(node1))


if __name__ == "__main__":
    main()
