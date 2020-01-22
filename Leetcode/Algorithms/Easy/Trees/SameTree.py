"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
"""
Input: two roots

Idea 1: recursively
Idea 2: iteratively

Output: bool if not true
"""


# Time Complexity: O(n)
# Space Complexity: O(n) -> due to placing on stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:
            return True
        elif not p or not q:
            return False        
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        


# Less clean solution

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if not s and not t:
            return True
        elif not s or not t:
            return False
        
        nodes_list = []
        find_dfs(s, t.val, nodes_list)
        
        if nodes_list:
            for node in nodes_list:
                if is_same_tree(node, t):
                    return True
        
        return False
    
def find_dfs(root, target, return_nodes):
    
    if root:        
        if root.val == target:
            return_nodes.append(root)
        
        find_dfs(root.left, target, return_nodes)
        find_dfs(root.right, target, return_nodes)    
        
    
    
def is_same_tree(root_one, root_two):
    
    if not root_one and not root_two:
        return True
    elif not root_one or not root_two:
        return False
    else:
        return root_one.val == root_two.val and is_same_tree(root_one.left, root_two.left) and is_same_tree(root_one.right, root_two.right)
