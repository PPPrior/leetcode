""" Depth-first Search """
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findParents(node):
            if node.left:
                parents[node.left.val] = node
                findParents(node.left)
            if node.right:
                parents[node.right.val] = node
                findParents(node.right)

        def findAns(node, source, depth):
            if not node:
                return
            if depth == k:
                ans.append(node.val)
                return
            if parents[node.val] != source:
                findAns(parents[node.val], node, depth + 1)
            if node.left != source:
                findAns(node.left, node, depth + 1)
            if node.right != source:
                findAns(node.right, node, depth + 1)
            pass

        parents = {root.val: None}
        ans = []
        findParents(root)
        findAns(target, None, 0)
        return ans
