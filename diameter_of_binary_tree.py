from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = -inf

        def dfs(node, sum):
            if not node:
                return 0

            if root.left:
                sum += 1
                dfs(node.left, sum)

            if root.right:
                sum += 1
                dfs(node.right, sum)

            return max(max_d, sum)

        return dfs(root, 0)

bst = TreeNode(1)
bst.right = TreeNode(2)
bst.right.left = TreeNode(3)
bst.right.left.left = TreeNode(3)
bst.right.right = TreeNode(4)

sol = Solution().diameterOfBinaryTree(bst)

print(sol)
