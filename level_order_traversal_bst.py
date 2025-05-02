from collections import deque
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
bst.right.left = BinaryTreeNode(7)
bst.right.right = BinaryTreeNode(8)

bst_one = BinaryTreeNode(0)


def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    q = deque([root])
    result = []

    while q:
        layer_len = len(q)
        layer = []

        for _ in range(layer_len):
            node = q.popleft()
            layer.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(layer)

    return result

print(level_order_traversal(bst))
print(level_order_traversal(bst_one))
