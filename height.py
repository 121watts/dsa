from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


tree = TreeNode(1)
tree_five = TreeNode(5)
tree_four = TreeNode(4)
tree_four.children = [TreeNode(100)]
tree_five.children = [tree_four]
tree.children = [TreeNode(2), TreeNode(3), tree_five]

def find_height(root):

    q = deque([root])
    level_count = 0

    while q:
        level_number = len(q)
        level_count += 1

        for _ in range(level_number):
            node = q.popleft()

            for child in node.children:
                q.append(child)

    return level_count - 1


print(find_height(tree))
