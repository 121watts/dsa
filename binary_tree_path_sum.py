class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def path_sum(root, target_sum):
    result = False

    def dfs(node, sum):
        nonlocal result

        if node is None:
            return None

        sum += node.val

        # we are at a leaf
        if node.left is None and node.right is None and sum == target_sum:
            result = True

        if node.left:
            dfs(node.left, sum)

        if node.right:
            dfs(node.right, sum)

    dfs(root, 0)

    return result

root = TreeNode(12, TreeNode(7, TreeNode(9)), TreeNode(1, TreeNode(10), TreeNode(5)))

# print(path_sum(root,  16))
print(path_sum(root,  23))
