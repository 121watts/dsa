
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_balanced_bst(a):
    if not a:
        return None

    mid = len(a) // 2
    root = BinaryTreeNode(a[mid].value)

    root.left = build_balanced_bst(a[:mid])
    root.right = build_balanced_bst(a[mid+1:])

    return root
