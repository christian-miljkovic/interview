"""
Chapter 4
Problem: Check if Binary Tree is Balanced
"""
import sys
sys.path.append('../../DataStructures')
from BinaryTree import Node as TreeNode

def isBalanced(root):
    
    try:
        isBalancedInternal(root)
        return True
    except:
        return False

def isBalancedInternal(root):

    if root == None:
        return -1

    else:
        leftTree = isBalancedInternal(root.left)
        rightTree = isBalancedInternal(root.right)

        difference = leftTree - rightTree
        
        if abs(difference) > 1:
            raise Exception("Binary Tree is not balanced")
        else:
            return max(isBalancedInternal(root.left), isBalancedInternal(root.right)) + 1


if __name__ == "__main__":
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n0.left = n1
    n0.right = n3

    # Un-comment to get an unbalanced tree
    # n4 = TreeNode(4)
    # n5 = TreeNode(5)    
    # n3.right = n4
    # n4.right = n5
    print(isBalanced(n0))