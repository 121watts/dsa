# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# binary tree is defined as for each node all nodes to the left of
# that node are less than and all nodes to the right are greater than
# so, we want to iterate over this sorted list
# the first node is the root
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
