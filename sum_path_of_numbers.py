class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findSumOfPathNumbers(self, root):
    def dfs(node, s):
        if not node:
            return None

        val = node.val

        if not node.left and not node.right:
            return int(s + str(val))

        left_val = dfs(node.left, s = s + str(val))
        right_val = dfs(node.right, s = s + str(val))

        return left_val + right_val

    return dfs(root, "")


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)


sol = Solution()
print(sol.findSumOfPathNumbers(root))
