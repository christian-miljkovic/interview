"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        node = root
        ans = (float('inf'),None)
        while node:
            diff = abs(target - node.val)
            if diff < ans[0]:
                ans = (diff, node.val)
            
            if node.val < target:                
                node = node.right
            else:
                node = node.left
                
        return ans[1]
