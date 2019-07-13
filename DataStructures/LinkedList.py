# Linked List Data Structure
# Adding is O(1)
# Finding and depending upon the implementation deletion is O(N)

class LinkedList:

    def __init__(self):
        self.head = None
        self.linkedListLength = 0
        
    
    def __str__(self):
        linked_list = []
        curr = self.head
        while curr != None:
            linked_list.append(curr.nodeData)
            curr = curr.nextNode
            
        return ''.join(str(data) + ' ' for data in linked_list)
    
    def addNode(self,data):
        if(self.head == None):
            self.head = Node(data)
            self.previousNode = None
        else:
            newNode = Node(data)
            newNode.nextNode = self.head
            self.head.previousNode = newNode
            self.head = newNode
            
        self.linkedListLength += 1
    
    def findNode(self,data):

        currentNode = self.head
        if(self.head == None):
            return None

        while(currentNode.nextNode != None):
            if(currentNode.nodeData == data):
                break
            else:
                currentNode = currentNode.nextNode
        
        return currentNode
                    
    def removeNode(self,data):

        nodeBeingRemoved = self.findNode(data)
        previousNode = nodeBeingRemoved.previousNode
        nextNode = nodeBeingRemoved.nextNode
        previousNode.nextNode = nextNode
        nextNode.previousNode = previousNode

class Node:

    def __init__(self, nodeData=None):
        if(nodeData == None):
            self.nodeData = None
        else:
            self.nodeData = nodeData
        
        self.nextNode = None
        self.previousNode = None

