""" Depth-first Search """
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, tmp):
            if not node:
                return
            if not (node.left or node.right):
                tmp += [node.val]
                tmp = [str(x) for x in tmp]
                ans.append(tmp)
            dfs(node.left, tmp + [node.val])
            dfs(node.right, tmp + [node.val])

        ans = []
        dfs(root, [])
        return ['->'.join(x) for x in ans]
