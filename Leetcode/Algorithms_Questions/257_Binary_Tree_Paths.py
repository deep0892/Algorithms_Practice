# https://leetcode.com/problems/binary-tree-paths/
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result: List[str] = []
        if(root == None):
            return result
        current_path: str = str(root.val)

        if(root.left == None and root.right == None):
            result.append(current_path)

        if(root.left != None):
            self.dfs(root.left, current_path, result)

        if(root.right != None):
            self.dfs(root.right, current_path, result)

        return result

    def dfs(self, root: TreeNode, current_path: str, result: List[str]) -> None:
        current_path += '->' + str(root.val)

        if(root.left == None and root.right == None):
            result.append(current_path)
            return

        if(root.left != None):
            self.dfs(root.left, current_path, result)

        if(root.right != None):
            self.dfs(root.right, current_path, result)


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node5 = TreeNode(5)
    node2.right = node5
    sol = Solution()
    print(sol.binaryTreePaths(node1))


if __name__ == "__main__":
    main()
