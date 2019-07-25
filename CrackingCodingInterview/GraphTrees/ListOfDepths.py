"""
Chapter 4 - Trees and Graphs
Problem - List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
Time Complexity: O(n)
Space Complexity: O(n)
"""
import sys
sys.path.append('../../DataStructures')
from LinkedList import Node as LinkedNode
from BinaryTree import Node as TreeNode

def setLinkedList(node, listOfHeads, index):
    if node != None:
        newNode = LinkedNode(node.data)
        if index < len(listOfHeads):
            if listOfHeads[index] == None:
                listOfHeads[index] = newNode
            else:
                listOfHeads[index].nextNode = newNode

def getDepth(root):
    if root == None:
        return 0
    else:
        return 1 + max(getDepth(root.left), getDepth(root.right))

def getListOfDepths(root, listOfHeads, depth):
    if root == None:
        return
    else:
        getListOfDepths(root.left, listOfHeads, depth + 1)
        getListOfDepths(root.right, listOfHeads, depth + 1)
        setLinkedList(root, listOfHeads, depth)

def printListOfLinkedLists(listOfLL):
    returnStr = ""
    for node in listOfLL:
        while node != None:
            returnStr += str(node.nodeData) + " "
            node = node.nextNode
        returnStr += '\n'
    print(returnStr)

if __name__ == "__main__":
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.left = n6
    depth = getDepth(n0)
    listOfHeads = [None] * depth
    getListOfDepths(n0, listOfHeads, 0)
    printListOfLinkedLists(listOfHeads)