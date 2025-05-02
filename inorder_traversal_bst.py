
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BinaryTreeNode(0)
bst.left = BinaryTreeNode(1)
bst.right = BinaryTreeNode(2)
bst.right.left = BinaryTreeNode(3)
# bst.left.right = BinaryTreeNode(4)


def inorder(root, result=[]):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """

    if not root:
        return result

    inorder(root.left)
    result.append(root.value)
    inorder(root.right)

    return result


print(inorder(bst))
