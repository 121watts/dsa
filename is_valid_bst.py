# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bst = TreeNode(5)
# bst.left = TreeNode(1)
# bst.right = TreeNode(7)
# bst.right.left = TreeNode(6)
# bst.right.right = TreeNode(8)
#
# bst = TreeNode(5)
# bst.left = TreeNode(1)
# bst.right = TreeNode(4)
# bst.right.left = TreeNode(3)
# bst.right.right = TreeNode(6)

bst = TreeNode(5)
bst.left = TreeNode(4)
bst.right = TreeNode(6)
bst.right.left = TreeNode(3)
bst.right.right = TreeNode(7)

def isValidBST(node: Optional[TreeNode]) -> bool:
    result_arr = []
    result = True

    def helper(root):
        if not root:
            return

        helper(root.left)
        result_arr.append(root.val)
        helper(root.right)

    helper(node)

    for index in range(len(result_arr) - 1):
        curr = result_arr[index]
        next = result_arr[index + 1]

        if curr >= next:
            result = False


    return result


print(isValidBST(bst))
