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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root:
            return []
        
        paths = []
        curr_path = str(root.val)
        
        pre_order_dfs(root.left, curr_path, paths)
        pre_order_dfs(root.right, curr_path, paths)
        
        if not paths:
            return curr_path
        
        return paths
        
        
def pre_order_dfs(root, curr_path, paths):
    
    if root:
        
        new_path = curr_path + "->" + str(root.val)
        if not root.left and not root.right:            
            paths.append(new_path)
            return paths
    
        pre_order_dfs(root.left, new_path, paths)
        pre_order_dfs(root.right, new_path, paths)
    
    return paths

        
        
        
       
        
        