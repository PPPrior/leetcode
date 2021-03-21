""" Breadth-first Search """
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, ans, l2r = [root], list(), 1
        while queue:
            n, level = len(queue), []
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                queue += [node.left] if node.left else []
                queue += [node.right] if node.right else []
            ans.append(level if l2r else level[::-1])
            l2r = not l2r
        return ans
