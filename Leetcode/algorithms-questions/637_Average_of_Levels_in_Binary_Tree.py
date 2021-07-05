# https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
Discription of question in above link
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    result = []
    if(root == None):
        return result

    queue = [root]
    while(len(queue) != 0):
        level_sum = 0
        size = len(queue)
        for i in range(0, size):
            current_node = queue.pop(0)
            level_sum += current_node.val
            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)

        double_level_avg = level_sum/size
        result.append(double_level_avg)

    return result


def main():
    """  Driver program to test the above function"""
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    print(averageOfLevels(root))


if __name__ == "__main__":
    main()
