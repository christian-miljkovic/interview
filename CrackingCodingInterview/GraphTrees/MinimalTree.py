"""
Chapter 4 Graph and Trees
Problem - Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""
import sys
sys.path.append('../../DataStructures')
from BinaryTree import Node

def createMinTree(array):
    
    if len(array) > 1:
        midPt = len(array)//2
        root = Node(array[midPt])
        print(array, array[midPt], midPt, array[:midPt])
        root.left = createMinTree(array[:midPt])
        root.right = createMinTree(array[midPt:])
        return root

def inOrderTraversal(root):
    if root != None:
        inOrderTraversal(root.left)
        print(root.data)
        inOrderTraversal(root.right)


testOrderedArray = [1,2,3,4,5,6,7]
headOfBST = createMinTree(testOrderedArray)
inOrderTraversal(headOfBST)