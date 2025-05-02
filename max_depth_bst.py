from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

bst = TreeNode(3)
bst.left = TreeNode(9)
bst.right = TreeNode(20)
bst.right.left = TreeNode(15)
bst.right.right = TreeNode(7)


def maxDepth(root: Optional[TreeNode], result=[], total=0) -> int:
    if not root:
        return total

    maxDepth(root.left, total + 1)
    maxDepth(root.right, total + 1)

    return [result, total]


print(maxDepth(bst))
