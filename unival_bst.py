
# For your reference:
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

bst = BinaryTreeNode(5)
bst.left = BinaryTreeNode(5)
# bst.left.left = BinaryTreeNode(5)
# bst.left.right = BinaryTreeNode(5)
# bst.right = BinaryTreeNode(5)
# bst.right.left = BinaryTreeNode(4)
# bst.right.right = BinaryTreeNode(5)

def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    count = 0

    def dfs(node):
        nonlocal count
        if not node:
            return True

        is_left_unival = dfs(node.left)
        is_right_unival = dfs(node.right)

        if is_left_unival and is_right_unival:
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False

            count += 1
            return True

        return False

    dfs(root)

    return count

print(find_single_value_trees(bst))
