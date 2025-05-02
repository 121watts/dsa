
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root_idx = inorder.index(root_val)

    root = TreeNode(root_val)

    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx+1:]

    left_preorder = preorder[1:1+len(left_inorder)]
    right_preorder = preorder[1+len(left_inorder):]

    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root

inorder = [2, 1, 3, 4]
preorder = [1, 2, 3, 4]

tree = buildTree(preorder, inorder)
print(tree.right.val)
