from typing import Optional
# dfs
# if not node1 and node2
#  node1 = node2
# if not node2 and node1:
#   node2 = node1
# if node1.val and node2.val
# node1.val = node1.val + node2.val

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2

        if root1 and not root2:
            return root1

        def helper(root1, root2):
            if not root1 and not root2:
                return None

            if (root1 and not root1.left) and (root2 and root2.left):
                root1.left = root2.left
                root2.left = 0

            if (root1 and not root1.right) and (root2 and root2.right):
                root1.right = root2.right
                root2.right = 0

            if root1 and root2:
                root1.val += root2.val
                self.mergeTrees(root1.left, root2.left)
                self.mergeTrees(root1.right, root2.right)


            return root1

        return helper(root1, root2)

root1 = None
root2 = TreeNode(1)

# root1 = TreeNode(1)
# root1.left = TreeNode(3)
# root1.left.left = TreeNode(5)
# root1.right = TreeNode(2)
#
# root2 = TreeNode(2)
# root2.left = TreeNode(1)
# root2.left.right = TreeNode(4)
# root2.right = TreeNode(3)
# root2.right.right = TreeNode(7)

sol = Solution()

result = sol.mergeTrees(root1, root2)

print(result)

# print('Left tree')
# print(result.val)
# print(result.left.val)
# print(result.left.left.val)
# print(result.left.right.val)
#
# print('Right Tree')
# print(result.right.val)
# print(result.right.right.val)
