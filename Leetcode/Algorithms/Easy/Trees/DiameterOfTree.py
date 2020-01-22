"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""

"""
Input: binary tree
Edge cases:
- root == None
- longest path between two nodes starts in a subtree
- unbalanced tree
- case given in example but 4 is not included

Output: The number of edges in the longest path

Idea: Something along the lines of shortest path by reversed
Brute force: Visit every node and then calculate the path len to each other node -> O(n^2)

1. Starting from root
2. Calculate the max depth of the right path and left path from each node
3. Loop through each node and see which has the greatest left + right value -> return that one
Time Complexity: O(n)
Space Complexity: O(n)


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diamater = [0]
        diameter_rec(root, diamater)
        
        return diamater[0]
        
def diameter_rec(root, diamater):
    
    if not root:
        return 0
    else:        
        left = diameter_rec(root.left, diamater)
        right = diameter_rec(root.right, diamater)
        diamater[0] = max(diamater[0], left + right)
        return 1 + max(left, right)
            
        



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution2(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        depth = dict()
        curr = root
        calc_depth(curr, depth)

        return calc_diameter(root, depth)
        
        
def calc_diameter(root, depth):
    
    if not root:
        return 0
    else:
        return max(depth[root][0] + depth[root][1], calc_diameter(root.left, depth),calc_diameter(root.right, depth))
        
    
        
def calc_depth(root, depth):
    
    if not root:
        return -1
    else:
        left_path = 1 + calc_depth(root.left, depth)
        right_path = 1 + calc_depth(root.right, depth)
        depth[root] = (left_path, right_path)
        return max(left_path, right_path)
    
        
        
        
        
        
        
        
        
        