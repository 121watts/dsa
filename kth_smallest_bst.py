
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BinaryTreeNode(2)
bst.left = BinaryTreeNode(1)
bst.right = BinaryTreeNode(3)

def kth_smallest_element(root, k):

    value = None
    count = 0

    def inorder(node):
        nonlocal count
        nonlocal value
        if not node:
            return

        inorder(node.left)

        count += 1
        if count == k:
            value = node.value
            return

        inorder(node.right)

    inorder(root)

    return value

print(kth_smallest_element(bst, 3))
