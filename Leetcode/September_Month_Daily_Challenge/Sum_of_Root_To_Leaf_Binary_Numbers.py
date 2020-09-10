# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/

"""
Problem Statement:
Given a binary tree, each node has value 0 or 1.  
Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, 
which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""

# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        sum = 0
        path = [] 
        sum = self.traverseTree(root, path, 0, sum)
        return sum
    
    def traverseTree(self, root, path, pathLen, sum): 
        print('start of traversal for root.val:', root.val, path, pathLen, sum)
        if root is None: 
            return sum
        if(len(path) > pathLen):  
            path[pathLen] = root.val 
        else: 
            path.append(root.val) 
        pathLen = pathLen + 1

        if root.left is None and root.right is None: 
            sum += int(''.join(str(e) for e in path[:pathLen]),2)
        else: 
           sum = self.traverseTree(root.left, path, pathLen, sum) 
           sum = self.traverseTree(root.right, path, pathLen, sum) 
        print('end of function of traversal for root.val', root.val, path, pathLen, sum)
        return sum
