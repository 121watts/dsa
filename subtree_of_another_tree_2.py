from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = True

        def is_equal(node, sub):
            nonlocal result
            if not node and not sub:
                return None

            if not node and sub:
                result = False
                return None

            if node and not sub:
                result = False
                return None

            if node.left.val != sub.left.val:
                result = False

            if node.right.val != sub.right.val:
                result = False

            is_equal(node.left, sub.left)
            is_equal(node.right, sub.right)

            return result


        def dfs(node):
            if not node:
                return None

            if node.val == subRoot.val:
                return is_equal(node, subRoot)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

sub = TreeNode(2)
sub.left = TreeNode(4)
sub.right = TreeNode(5)

sol = Solution().isSubtree(root, sub)
print(sol)
