from collections import deque

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

def zigzag(root):
    q = deque([root])
    result = []

    while q:
        level_len = len(q)
        level = []

        for _ in range(level_len):
            level_number = len(result) + 1
            is_even_level = level_number % 2 == 0
            node = None

            if is_even_level:
                node = q.pop()
            else:
                node = q.popleft()

            level.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result

print(zigzag(bst))
