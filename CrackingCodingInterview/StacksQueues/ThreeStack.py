"""
Chapter 3 Stack and Queue Problems
Problem: Implement 3 stacks using one array
"""

class TripleStack:

    def __init__(self):
        self.stack = [None] * 30
        self.topA = 0
        self.topB = 1
        self.topC = 2

    def isAtCapacity(self):
        size = len(self.stack)
        return self.topA >= size or self.topB >= size or self.topC >= size
    
    def reSize(self):
        newList = [None] * len(self.stack)
        self.stack.extend(newList)
    
    def insert(self, stack, data):
        if self.isAtCapacity():
            self.reSize()
            self.insertInternal(stack, data)
        else:
            self.insertInternal(stack, data)

    def insertInternal(self, stack, data):        
        if stack == 'A':
            self.stack[self.topA] = data
            self.topA += 3
        elif stack == 'B':
            self.stack[self.topB] = data
            self.topB += 3
        else:
            self.stack[self.topC] = data
            self.topC += 3
    
    def pop(self, stack):
        
        returnData = None

        if stack == 'A' and self.topA > 0:
            returnData = self.stack[self.topA]
            self.stack[self.topA] = None
            self.topA -= 3
        elif stack == 'B' and self.topB > 1:
            returnData = self.stack[self.topB]
            self.stack[self.topB] = None
            self.topB -= 3
        elif stack == 'C' and self.topC > 2:
            returnData = self.stack[self.topC]
            self.stack[self.topC] = None
            self.topC -= 3        

        return returnData

    def __str__(self):
        stackA = []
        stackB = []
        stackC = []
        
        topA = self.topA
        topB = self.topB
        topC = self.topC
        while topA >= 0 and topB >= 1 and topC >= 2:
            stackA.append(self.stack[topA])
            stackB.append(self.stack[topB])
            stackC.append(self.stack[topC])
            topA -= 3
            topB -= 3
            topC -= 3

        
        strStackA = ' '.join(str(num) for num in stackA if num != None)
        strStackB = ' '.join(str(num) for num in stackB if num != None)
        strStackC = ' '.join(str(num) for num in stackC if num != None)
        return 'Stack A: ' + strStackA + '\n' + 'Stack B: ' + strStackB + '\n' + 'Stack C: ' + strStackC

if __name__ == "__main__":
    testTripleStack = TripleStack()
    testTripleStack.insert('A', 1)
    testTripleStack.insert('A', 2)
    testTripleStack.insert('A', 3)
    testTripleStack.insert('B', 4)
    testTripleStack.insert('B', 5)
    testTripleStack.insert('B', 6)
    testTripleStack.insert('C', 8)
    testTripleStack.insert('C', 9)
    testTripleStack.insert('C', 10)
    testTripleStack.insert('A', 11)
    testTripleStack.insert('B', 12)
    testTripleStack.insert('C', 13)
    print(testTripleStack)
    print('')
    testTripleStack.pop('A')
    testTripleStack.pop('B')
    testTripleStack.pop('C')
    testTripleStack.pop('A')
    testTripleStack.pop('B')
    testTripleStack.pop('C')
    print(testTripleStack)
