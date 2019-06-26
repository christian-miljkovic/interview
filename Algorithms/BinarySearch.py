import sys
sys.path.append('../DataStructures')
from BinaryTree import BinaryTree

def binarySearchRecursive(root, data):

    if(root.data == data):
        return True
    else:
        if(root.data >= data):
            if(root.left == None):
                return False
            return binarySearchRecursive(root.left, data)

        else:
            if(root.right == None):
                return False
            return binarySearchRecursive(root.right, data)

def binarySearchIterative(root, data):

    while(root != None):
        if(root.data == data):
            return True
        if(root.data >= data):
            root = root.left
        else:
            root = root.right
    else:
        return False

if __name__ == '__main__':
    binaryTree = BinaryTree()
    binaryTree.insert(5)
    binaryTree.insert(12)
    binaryTree.insert(11)
    binaryTree.insert(3)
    binaryTree.insert(4)
    binaryTree.insert(1)
    print(binaryTree.toString())
    print(binarySearchRecursive(binaryTree.root, 12))
    print(binarySearchRecursive(binaryTree.root, 2))
    print(binarySearchIterative(binaryTree.root, 12))
    print(binarySearchIterative(binaryTree.root, 2))    