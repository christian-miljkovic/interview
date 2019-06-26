# Class to implement binary tree

class BinaryTree:

    def __init__(self):
        self.root = None
        self.preOrderList = []

    def insert(self, data):
        if(data == None):
            return
        else:
            if(self.root == None):
                self.root = Node(data)
            else:
                newNode = Node(data)
                self.insertInternal(self.root, newNode)

    def insertInternal(self, root, node):
        if(root == None):
            root = node
        else:
            if(root.data >= node.data):
                if(root.left is None):
                    root.left = node
                else:
                    self.insertInternal(root.left, node)
            else:
                if(root.right is None):
                    root.right = node
                else:
                    self.insertInternal(root.right, node)


    def toString(self):
        self.preOrder(self.root)
        return self.preOrderList
    
    def preOrder(self, node):
        if(node != None):
            # to do in-order or post-order you just move the append either in the middle
            # of the node.left and node.right calls or at the end of all the recursive calls
            self.preOrderList.append(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)
            

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 0

if __name__ == '__main__':
    testBTree = BinaryTree()
    testBTree.insert(5)
    testBTree.insert(3)
    testBTree.insert(10)
    testBTree.insert(1)
    testBTree.insert(2)
    testBTree.insert(16)
    testBTree.insert(18)
    testBTree.insert(14)
    print(testBTree.toString())