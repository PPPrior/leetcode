""" Breadth-first Search """
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        queue, ans = [root], list()
        while queue:
            n, level = len(queue), []
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                queue.extend(node.children)
            ans.append(level)
        return ans
