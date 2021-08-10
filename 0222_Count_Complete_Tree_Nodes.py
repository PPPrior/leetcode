""" Binary Search """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def exist(id):
            bits = 1 << (level - 2)
            node = root
            while node and bits > 0:
                if id & bits:
                    node = node.right
                else:
                    node = node.left
                bits >>= 1
            return node

        level = 0
        node = root
        while node:
            level += 1
            node = node.left

        lo, hi = 2 ** (level - 1), 2 ** level - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if exist(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
