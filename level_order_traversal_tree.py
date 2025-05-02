from collections import deque
# For your reference:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

tree = TreeNode(1)
tree_four = TreeNode(4)
tree_four.children = [TreeNode(5), TreeNode(6)]
tree.children = [TreeNode(3), tree_four, TreeNode(2)]

def level_order(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     list_list_int32
    """

    result = []
    q = deque([root])

    while q:
        level_len = len(q)
        level = []
        for _ in range(level_len):
            node = q.popleft()
            level.append(node.value)

            for child in node.children:
                q.append(child)

        result.append(level)

    return result

print(level_order(tree))
