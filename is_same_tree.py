from typing import Optional

# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tq = TreeNode(1)
tq.left = TreeNode(2)
tq.right = TreeNode(3)

tp = TreeNode(1)
tp.left = TreeNode(2)
tp.right = TreeNode(4)

# traverse down each tree simultaneously using the same order
# if at anypoint the current node values are not the same then set
# value to False
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    is_same = True

    def dfs(p, q):
        nonlocal is_same
        if (not p and q) or (p and not q):
            is_same = False
            return

        if not p and not q:
            return

        if p.val != q.val:
            is_same = False
            return

        dfs(p.left, q.left)
        dfs(p.right, q.right)


    dfs(p, q)

    return is_same

print(isSameTree(tq, tp))
