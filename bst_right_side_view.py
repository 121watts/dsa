from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


bst = TreeNode(1)
bst.left = TreeNode(2)
bst.left.right = TreeNode(5)
bst.left.left = TreeNode(4)
bst.right = TreeNode(3)

# bst = None

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result = []

    if not root:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level_nodes[-1])

    return result


print(right_side_view(bst))
