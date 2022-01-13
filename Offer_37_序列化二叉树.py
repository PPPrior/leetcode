""" Depth-first Search """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'X'
        leftser = self.serialize(root.left)
        rightser = self.serialize(root.right)
        return str(root.val) + ' ' + leftser + ' ' + rightser

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')

        def dfs(data):
            val = data.pop(0)
            if val == 'X':
                return None
            else:
                node = TreeNode(int(val))
                node.left = dfs(data)
                node.right = dfs(data)
            return node

        return dfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
