# Binary Search Tree Data Strucutre
# The whole log(n) figure comes from if you think about how you are taking about magnitutdes 
# so each level you are increasing the number of nodes by that magnitude
# First level you have one, then next level you have x^level so it is increasing by a magnitude of the level variable
# Then if you think about the search if you say log(x) if you have 16 nodes it will take at most 4 actions to find what 
# you are looking for. Where base 2 of log(x) we will get that x = 4 because log(x) is looking for base^x -> in this 
# case that I just gave you would get 2^4 (for a binary search tree)
# Deletion is O(h)

class TreeNode():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    # 0(h) runtime
    def add(self,root,data):
        if(data == None):
            return None
        if(root == None):
            root = TreeNode(data)
            return root
        else:
            if(root.data >= data):
                root.left = root.add(root.left, data)
            else:
                root.right = root.add(root.right, data)
    # 0(h) runtime
    def find(self,root, data):
        if(data == None):
            return None
        if(root.data == data):
            return root.data
        elif(root.data > data):
            root.find(root.left,data)
        else:
            root.find(root.right,data)
    
    # This is wrong
    def inOrderTraversal(self,root):
        if(root != None):        
            if(root.left == None and root.right == None):
                print(root)
            elif(root.left != None):
                self.inOrderTraversal(root.left)
            else:
                self.inOrderTraversal(root.right)
    
    # The base case check of checking if the root is not null allows you to make it cleaner
    def inOrderTraversalCorrect(self,root):
        if(root != None):
            self.inOrderTraversalCorrect(root.left)
            print(root.data)
            self.inOrderTraversalCorrect(root.right)
            

    def preOrderTraversal(self,root):
        if(root != None):
            print(root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def postOrderTraversal(self,root):
        if(root != None):
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)
            print(root.data)