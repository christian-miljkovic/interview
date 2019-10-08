"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

"""
# New cleaner attempt
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return is_same(root.left, root.right)
        
        
def is_same(left_node, right_node):
    
    if not left_node and not right_node:
        return True
    elif not left_node or not right_node:
        return False
    else:
        return left_node.val == right_node.val and is_same(left_node.right, right_node.left) and is_same(left_node.left, right_node.right)




# Successful Attempt
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return is_symetric(root.left, root.right)
        
def is_symetric(left_root, right_root):
    
    if left_root == None and right_root == None:
        return True
    elif (left_root == None and right_root != None) or (left_root != None and right_root == None):
        return False
    elif left_root.val != right_root.val:
        return False
    else:
        left_tree = is_symetric(left_root.right, right_root.left)
        right_tree = is_symetric(left_root.left, right_root.right)
        return left_tree and right_tree

# Failed Attempt

"""
Edge cases: null -> should return false, one element -> true
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            left_path = []
            right_path = []
            print(left_dfs(root.left,left_path),right_dfs(root.right,right_path))
            if left_dfs(root.left,left_path) == right_dfs(root.right,right_path):
                return True
            
            return False
            
        return True
        
def left_dfs(root,path):
    
    if not root:
        path.append(None)
    
    else:
        path.append(root.val)
        left_dfs(root.left, path)
        left_dfs(root.right, path)
    
    return path

def right_dfs(root,path):
    
    if not root:
        path.append(None)
    
    else:
        path.append(root.val)
        left_dfs(root.right, path)
        left_dfs(root.left, path)

    return path
        