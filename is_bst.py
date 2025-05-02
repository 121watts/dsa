class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# inorder traversal should always increase

bst = BinaryTreeNode(5)
bst.left = BinaryTreeNode(4)
bst.right = BinaryTreeNode(6)
bst.left.left = BinaryTreeNode(100)

def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """

    values = []
    result = True

    def dfs(node):
        if not node:
            return None

        dfs(node.left)
        values.append(node.value)
        dfs(node.right)

    dfs(root)

    for i in range(len(values) - 1):
        if values[i] >= values[i + 1]:
            result = False

    # Write your code here.
    return result

print(is_bst(bst))
