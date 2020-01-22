"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    
    def pathSum(self, root: TreeNode, sum: int) -> int:        
        
        if not root:
            return 0
        
        paths = [0]
        dfs(root, sum, paths)
        
        return paths[0]

def dfs(root, target, paths):

    if root:

        nested_dfs(root, 0, target, paths)
        dfs(root.left, target, paths)
        dfs(root.right, target, paths)

    
def nested_dfs(root, curr_sum, target, paths):

    if root:

        if target == curr_sum + root.val:
            paths[0] += 1

        nested_dfs(root.left, curr_sum + root.val, target, paths)
        nested_dfs(root.right, curr_sum + root.val, target, paths)
            