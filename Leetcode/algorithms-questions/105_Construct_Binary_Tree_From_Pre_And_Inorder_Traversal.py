# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
Discription of question in above link
Depth First Traversals:
(a) Inorder (Left, Root, Right) 
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    return helper(0, 0, len(inorder)-1, preorder, inorder)


def helper(preStart, inStart, inEnd, preorder, inorder):
    if(preStart > len(preorder)-1 or inStart > inEnd):
        return None
    root = TreeNode(preorder[preStart])
    inIndex = 0
    for i in range(inStart, inEnd+1):
        if inorder[i] == root.val:
            inIndex = i
    root.left = helper(preStart + 1, inStart, inIndex - 1, preorder, inorder)
    root.right = helper(preStart + inIndex - inStart + 1,
                        inIndex + 1, inEnd, preorder, inorder)

    return root


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(buildTree(preorder, inorder))


if __name__ == "__main__":
    main()
