# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs into root
# if we hit a node in root that has the same value as subRoot's root
# we check if they are the same tree

tree_root = TreeNode(3)
# tree_root.left = TreeNode(4)
# tree_root.left.left = TreeNode(1)
# tree_root.left.right = TreeNode(2)
# # uncomment for unequal case
# # tree_root.left.right.right = TreeNode(100)
# tree_root.right = TreeNode(5)

tree_sub = TreeNode(4)
# tree_sub.left = TreeNode(1)
# tree_sub.right = TreeNode(2)



def isSubtree(root, subRoot) -> bool:
    is_same_tree = True

    if not root.left and not root.right:
        if root.val != subRoot.val:
            return False

    def is_same(node, subRoot):
        nonlocal is_same_tree
        if not node and not subRoot:
            return

        if not node and subRoot:
            is_same_tree = False
            return

        if node and not subRoot:
            is_same_tree = False
            return

        if node.val != subRoot.val:
            is_same_tree = False
            return

        is_same(node.left, subRoot.left)
        is_same(node.right, subRoot.right)

    def dfs(node):
        nonlocal is_same_tree
        if not node:
            return None

        if node.val == subRoot.val:
            is_same(node, subRoot)
            return

        dfs(node.left)
        dfs(node.right)

        # is_same_tree = False


    dfs(root)

    return is_same_tree

print(isSubtree(tree_root, tree_sub))
