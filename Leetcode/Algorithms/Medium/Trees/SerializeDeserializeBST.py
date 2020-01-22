"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        self.r_serialize(root, path)
        return ','.join(path)
        
    def r_serialize(self, root, path):
        
        if not root:
            path.append(str(None))
        else:
            path.append(str(root.val))
            self.r_serialize(root.left, path)
            self.r_serialize(root.right, path)
        
        return path
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        path = data.split(',')
        path = collections.deque(path)
        return self.r_deserialize(path)
    
    def r_deserialize(self, path):
        
        if path[0] == 'None':
            path.popleft()
            return None
        
        root = TreeNode(int(path[0]))
        path.popleft()
        root.left = self.r_deserialize(path)
        root.right = self.r_deserialize(path)
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))