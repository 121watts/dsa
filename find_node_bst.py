"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """

    if not root:
        return False

    def dfs(node):
        if not node:
            return False

        if value < node.value:
            return dfs(node.left)
        elif value > node.value:
            return dfs(node.right)
        else:
            return True

    return dfs(root)
