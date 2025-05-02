from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def dfs(node, height):
            nonlocal result
            if not node:
                return 0

            left_height = dfs(node.left, height + 1)
            right_height = dfs(node.right, height + 1)

            print(left_height, right_height)

            if abs(left_height - right_height) > 1:
                result = False

            return 1 + max(left_height, right_height)

        dfs(root, 0)

        return result


bst = TreeNode(1)
bst.left = TreeNode(2)
bst.right = TreeNode(3)
bst.right.left = TreeNode(4)
bst.right.left.left = TreeNode(5)

sol = Solution().isBalanced(bst)
print(sol)
