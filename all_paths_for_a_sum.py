class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def findPaths(root, target_sum):
  allPaths = []

  def helper(node, sum, path):
    nonlocal allPaths

    if not node:
        return None

    sum += node.val
    path.append(node.val)

    is_leaf = node.left is None and node.right is None

    if is_leaf and sum == target_sum:
        allPaths.append(path)

    helper(node.left, sum, list(path))
    helper(node.right, sum, list(path))

  helper(root, 0, [])

  return allPaths

root = TreeNode(12)
root.left = TreeNode(7)
root.left.left = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(findPaths(root, 23))
