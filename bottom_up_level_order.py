from collections import deque
# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BinaryTreeNode(0)
bst.left = BinaryTreeNode(1)
bst.left.left = BinaryTreeNode(3)
bst.left.right = BinaryTreeNode(4)
bst.right = BinaryTreeNode(2)

def reverse_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    q = deque([root])
    levels = []

    while q:
        level_len = len(q)
        level = []

        for _ in range(level_len):
            node = q.popleft()
            level.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        levels.insert(0, level)

    return levels

print(reverse_level_order_traversal(bst))
