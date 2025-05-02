# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


bst = TreeNode(3)
bst.left = TreeNode(3)
bst.left.left = TreeNode(4)
bst.left.right = TreeNode(2)
# bst.right = TreeNode(4)
# bst.right.right = TreeNode(5)
# bst.right.left = TreeNode(1)

def good_nodes(root, result=[], max=float('-inf')):
    if not root:
        return

    if root.val >= max:
        max = root.val
        result.append(root.val)

    good_nodes(root.left, result, max)
    good_nodes(root.right, result, max)

    return len(result)
