"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

"""
Input: two binary trees not BST's

Output: bool if t is a subtree of s
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if not s or not t:
            return False
        
        
        subtree_root_list = find_nodes(s, t.val, root_list=[])

        if subtree_root_list:
            for root in subtree_root_list:
                if is_same(root, t):
                    return True
        
        return False
        
def find_nodes(root, target_val, root_list):
    
    if root:
       
        if root.val == target_val:
            root_list.append(root)    
            
        
        find_nodes(root.left, target_val, root_list)
        find_nodes(root.right, target_val, root_list)
        
    return root_list
            
def is_same(root_one, root_two):
    
    if not root_one and not root_two:
        return True
    
    elif not root_one or not root_two:
        return False
    else:
        return root_one.val == root_two.val and is_same(root_one.left, root_two.left) and is_same(root_one.right, root_two.right)
    