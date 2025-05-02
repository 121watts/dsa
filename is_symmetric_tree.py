import copy
# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BinaryTreeNode(1)
# bst.left = BinaryTreeNode(2)
# bst.left.left = BinaryTreeNode(3)
# bst.left.right = BinaryTreeNode(4)
# bst.right = BinaryTreeNode(2)
# bst.right.left = BinaryTreeNode(4)
# bst.right.right = BinaryTreeNode(3)


def check_if_symmetric(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """

    is_symmetric = True

    def invert(node):
        if not node:
            return node

        left = node.left
        right = node.right

        node.left = right
        node.right = left

        invert(node.left)
        invert(node.right)

    invert(root.right)

    def is_same(lsub, rsub):
        nonlocal is_symmetric
        if not lsub and not rsub:
            return

        if (lsub and not rsub) or (rsub and not lsub):
            is_symmetric = False
            return

        if lsub.value != rsub.value:
            is_symmetric = False
            return

        is_same(lsub.left, rsub.left)
        is_same(lsub.right, rsub.right)

    is_same(root.left, root.right)

    return is_symmetric

print(check_if_symmetric(bst))
