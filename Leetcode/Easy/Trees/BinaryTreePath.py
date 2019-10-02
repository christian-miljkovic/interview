"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        return get_leaf_node_path(root, "", paths)
        
def get_leaf_node_path(root, current_path, paths):
    
    if root:

        current_path += str(root.val)
        
        if not root.right and not root.left:
            paths.append(current_path)
        else:
            current_path += '->'
            get_leaf_node_path(root.left, current_path, paths)
            get_leaf_node_path(root.right, current_path, paths)
            
    return paths