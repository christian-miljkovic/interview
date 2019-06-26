# Stack Data Structure
# O(1) remove and insertions
# O(n) find 

class Stack():

    def __init__(self):
        self.stack = []
        self.index = -1
    
    def push(self,item):
        self.stack.append(item)
        self.index += 1
    
    def pop(self):
        if(self.index < 0):
            return None
        item = self.stack[self.index]
        self.stack = self.stack[:self.index]
        return item
    
    def peek(self):
        return self.stack[self.index]

    def isEmpty(self):
        return self.index >= 0
