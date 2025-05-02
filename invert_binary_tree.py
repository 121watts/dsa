from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            left = node.left
            right = node.right

            node.right = left
            node.left = right

            dfs(node.left)
            dfs(node.right)

            return node

        return dfs(root)


bst = TreeNode(1)
bst.left = TreeNode(2)
bst.left.left = TreeNode(4)
bst.left.right = TreeNode(5)
bst.right = TreeNode(3)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(7)

sol = Solution().invertTree(bst)

print(sol.val)
print(sol.left.val)
print(sol.left.left.val)
print(sol.right.val)
print(sol.right.right.val)
