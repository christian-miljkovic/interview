"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Compelxity: O(log(n) * log(n)) because finding the depth is log(n) in a complete tree ***finding a path
# in a tree is log(n) and then since you are choosing between left or right it is again log(n)
# Space Complexity: O(log(n))

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        if left_depth == right_depth:
            return (2**left_depth) + self.countNodes(root.right)
            
        else:
            return (2**right_depth) + self.countNodes(root.left)
    
    
def get_depth(root):
    
    depth = 0
    while root:
        depth += 1
        root = root.left
    
    return depth 