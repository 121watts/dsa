# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BinaryTreeNode(0)
bst.left = BinaryTreeNode(1)
bst.right = BinaryTreeNode(2)
bst.left.left = BinaryTreeNode(3)
bst.left.right = BinaryTreeNode(4)

def postorder(root, result=[]):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """

    if not root:
        return result

    postorder(root.left)
    postorder(root.right)
    result.append(root.value)

    return result


print(postorder(bst))
