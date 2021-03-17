""" Depth-first Search """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        h = 10 ** 6
        if root.left:
            h = min(h, self.minDepth(root.left))
        if root.right:
            h = min(h, self.minDepth(root.right))
        return h + 1
