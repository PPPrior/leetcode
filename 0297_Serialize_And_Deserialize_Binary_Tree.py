""" Breadth-first Search """


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
            return ''
        queue, ser = [root], []
        while queue:
            node = queue.pop(0)
            if node:
                ser.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ser.append('X')
        return ' '.join(map(str, ser))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(' ')
        root = TreeNode(int(data.pop(0)))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                val = data.pop(0)
                if val != 'X':
                    node.left = TreeNode(val)
                    queue.append(node.left)
            if node:
                val = data.pop(0)
                if val != 'X':
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
