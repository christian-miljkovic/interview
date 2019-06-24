# Class to implement binary tree

class BinaryTree:

    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if(data == None):
            return
        else:
            self.insertInternal(self.root, data)

    def insertInternal(self, node, data):
        if(node == None):
            node = Node(data)
            print(node)
        else:
            if(node.data >= data):
                self.insertInternal(node.left, data)
            elif(node.data < data):
                self.insertInternal(node.right, data)

    def toString(self):
        return self.preOrder(self.root)
    
    def preOrder(self, node):
        preOrderList = []
        if(node != None):
            preOrderList.append(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 0

testBTree = BinaryTree()
testBTree.insert(5)
testBTree.insert(3)
testBTree.insert(7)
testBTree.insert(1)
testBTree.insert(2)
testBTree.insert(6)
testBTree.insert(8)
print(testBTree.toString())