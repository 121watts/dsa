from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root_bst = TreeNode(3)
# root_bst.left = TreeNode(4)
# root_bst.left.left = TreeNode(1)
# root_bst.left.right = TreeNode(2)
# root_bst.right = TreeNode(5)

sub_bst = TreeNode(3)
# sub_bst.left = TreeNode(1)
# sub_bst.right = TreeNode(2)

# nope = TreeNode(4)
# nope.left = TreeNode(3)
# nope.right = TreeNode(2)

# if we hit a node that's the same val as the subRoot's root val
# start a recursion of both subRoot and root
# compare nodes as we dfs or bfs through the tree
# if at any point we they aren't equal return
# bfs is more intuitive for me once we hit the same root val
# ill start with a dfs to uncover the common node then bfs over subroot

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return

            if node.val == subRoot.val:
                return bfs(node, subRoot)

            return dfs(root.left) or dfs(root.right)

        return dfs(root)

def bfs(root, subRoot):
    root_q = deque([root])
    sub_q = deque([subRoot])

    while sub_q:
        r_node = root_q.popleft()
        sub_node = sub_q.popleft()

        if not r_node or not sub_node:
            if r_node != sub_node:
                return False

            continue

        if r_node.val != sub_node.val:
            return False

        root_q.append(r_node.left)
        sub_q.append(sub_node.left)

        root_q.append(r_node.right)
        sub_q.append(sub_node.right)

    return True


print(isSubtree(root_bst, sub_bst))
