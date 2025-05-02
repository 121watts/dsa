from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(2)
bst.left.right = TreeNode(4)
bst.left.left.left = TreeNode(1)

bst.right = TreeNode(6)


def kthSmallest(root: Optional[TreeNode], k: int) -> int:

    result_arr = []
    result = -1

    def inorder(node: Optional[TreeNode]):
        if not node:
            return

        inorder(node.left)
        result_arr.append(node.val)
        inorder(node.right)


    inorder(root)

    if len(result_arr):
        result = result_arr[k - 1]

    return result



print(kthSmallest(bst, 3))
