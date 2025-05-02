
# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BinaryTreeNode(1)
bst.left = BinaryTreeNode(2)
bst.right = BinaryTreeNode(3)
bst.left.left = BinaryTreeNode(4)
bst.left.right = BinaryTreeNode(5)
bst.left.right.left = BinaryTreeNode(7)
bst.left.right.left.right = BinaryTreeNode(8)
bst.left.left.left = BinaryTreeNode(5)

def height_of_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root:
        return 0

    left_depth = 1 + height_of_binary_tree(root.left)
    right_depth = 1 + height_of_binary_tree(root.right)

    return max(left_depth, right_depth)

print(height_of_binary_tree(bst))
