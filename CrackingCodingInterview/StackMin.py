"""
Chapter 3 Stacks and Queue
Problem - Stack Min: How would you design a stack which, in addition to push and pop, 
has a function min which returns the minimum element? Push, pop, and min should all operate in min O(1) time
"""

class MinStack():

    def __init__(self):
        self.stack = []
        self.top = 0
    
    def push(self, data):
        if len(self.stack) == 0:
            self.stack.append(data)
        else:
            prev = self.pop()
            if prev >= data:
                self.stack.append(prev)
                self.stack.append(data)
                self.top += 2
            else:
                self.stack.append(data)
                self.stack.append(prev)
                self.top += 2
    
    def getMin(self):
        return self.stack[self.top]
    
    def pop(self):
        returnVal = self.stack[self.top]
        self.stack = self.stack[:self.top]
        self.top -= 1
        return returnVal

if __name__ == "__main__":
    testMinStack = MinStack()
    testMinStack.push(5)
    testMinStack.push(1)
    testMinStack.push(2)
    testMinStack.push(3)
    print(testMinStack.getMin())
    testMinStack.pop()
    print(testMinStack.getMin())

            