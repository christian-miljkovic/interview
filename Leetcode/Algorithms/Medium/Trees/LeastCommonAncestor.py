"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        create_path(root, p, p_path)
        create_path(root, q, q_path)
        
        p_path = p_path[::-1]
        q_path = q_path[::-1]
        last_same_node = p_path[0]
        i = 1
        j = 1
        
        while i < len(p_path) and j < len(q_path):
            if p_path[i] != q_path[j]:
                return last_same_node
            
            last_same_node = p_path[i]            
            i += 1
            j += 1
        
        
        return last_same_node
        
        
def create_path(root, target_node, path):
    
    if root:
        
        if root.val == target_node.val:
            path.append(root)
            return True
        
        if create_path(root.left, target_node, path) or create_path(root.right, target_node, path):
            path.append(root)
            return True
        
        return False
        
    
        