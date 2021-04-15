""" Depth-first Search """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def houseRobber(node):
            if not node:
                return [0, 0]
            left = houseRobber(node.left)
            right = houseRobber(node.right)
            return [node.val + left[1] + right[1], max(left) + max(right)]

        return max(houseRobber(root))
