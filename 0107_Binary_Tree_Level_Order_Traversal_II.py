""" Breadth-first Search """
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, ans = [root], list()
        while queue:
            n, level = len(queue), []
            for _ in range(n):
                node = queue.pop(0)
                queue += [node.left] if node.left else []
                queue += [node.right] if node.right else []
                level.append(node.val)
            ans.append(level)
        return ans[::-1]
