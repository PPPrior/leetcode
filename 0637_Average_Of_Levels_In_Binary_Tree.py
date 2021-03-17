""" Breadth-first Search """
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue, ans = [root], list()
        while queue:
            n, sum = len(queue), 0
            for _ in range(n):
                node = queue.pop(0)
                queue += [node.left] if node.left else []
                queue += [node.right] if node.right else []
                sum += node.val
            ans.append(sum / n)
        return ans
