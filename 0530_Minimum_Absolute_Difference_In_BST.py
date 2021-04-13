""" Depth-first Search """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def traversal(node):
            if not node:
                return
            nonlocal ans
            traversal(node.left)
            seq.append(node.val)
            if len(seq) >= 2:
                ans = min(ans, seq[-1] - seq[-2])
            traversal(node.right)

        seq, ans = [], float('inf')
        traversal(root)
        return int(ans)
