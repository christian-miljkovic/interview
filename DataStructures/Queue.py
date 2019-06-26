# Queue data structure built using linked list
# FIFO: O(1) inseration and removal

class Queue():

    def __init__(self):
        self.front = None
        self.back = None

    # Efficient way of doing it
    def add(self, item):
        node = Node(item)
        if(self.back == None):
            self.back = node
            self.front = node
        else:
            self.back.next = node
            self.back = self.back.next

    def remove(self):
        if(self.front == None):
            return None
        returnData = self.front.data
        self.front = self.front.next
        return returnData

    def peek(self):
        if(self.front == None):
            return None
        return self.front.data

    def isEmpty(self):
        return self.front == None and self.back == None

    # Inefficient way of doing it
    def add2(self,item):
        node = Node(item)
        if(self.front == None):
            self.front = node
            self.back = node
        else:
            node.next = self.back
            self.back = node
        
    def remove2(self):
        if(self.front == None):
            return None
        currentNode = self.back
        while(currentNode.next != self.front):
            currentNode = currentNode.next
        
        returnNode = currentNode.next
        currentNode.next = None
        return returnNode

    def peek2(self):
        if(self.back == None):
            return None
        currentNode = self.back
        while(currentNode.next == None):
            currentNode = currentNode.next

        return currentNode 


class Node():

    def __init__(self,data=None):
        self.next = None
        self.data = data