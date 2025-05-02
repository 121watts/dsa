class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# bst = BinaryTreeNode(0)
# bst.left = BinaryTreeNode(1)
# bst.right = BinaryTreeNode(2)
# bst.left.left = BinaryTreeNode(3)
# bst.left.right = BinaryTreeNode(4)

bst = None

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    result = []

    if not root:
        return result

    def dfs(node):
        if not node:
            return

        result.append(node.value)
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return result


print(preorder(bst))
