"""
Chapter 3 Stacks and Queues
Problem - Stack of Plates: Imagine a literal stack of paltes. If the stack gets too high, it might topple.
Therefore, in real life we would likely start a new stack when previous stack exceeds some threshold. Implement
a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create
a new stack once the previous one exceeds capacity. Push() and pop() should should behave identically to a single stack.
"""

class SetOfStacks:

    def __init__(self):
        self.stack_list = []
        self.curr_stack_index = -1
    
    def addStack(self):
        new_stack = Stack()
        self.stack_list.append(new_stack)
        self.curr_stack_index += 1
    

    def push(self, data):

        if self.curr_stack_index < 0:
            self.addStack()

        curr_stack = self.stack_list[self.curr_stack_index]
        if curr_stack.isAtCapacity():
            self.addStack()
            
        curr_stack = self.stack_list[self.curr_stack_index]
        curr_stack.push(data)

    def pop(self):
        if self.curr_stack_index < 0:
            raise Exception("SetOfStacks is empty")
        if self.stack_list[self.curr_stack_index].size == 0:
            self.stack_list = self.stack_list[:self.curr_stack_index]
            self.curr_stack_index -= 1
            
        return self.stack_list[self.curr_stack_index].pop()

    
    def __str__(self):
        
        return_str = ""
        
        for stack in self.stack_list:
            return_str += ' '.join(str(num) for num in stack.array) + '\n'
            
        return return_str

class Stack:

    def __init__(self):
        self.array = [None] * 3
        self.top = -1
        self.size = 0

    def push(self, data):
        if data == None:
            raise Exception("Data is null")
        # Don't need to check capacity here because if it is reached the SetOfStacks will create a new one
        self.top += 1
        self.array[self.top] = data
        self.size += 1
    
    def pop(self):
        if self.size <= 0:
            raise Exception("Stack is empty")    
        return_val = self.array[self.top]
        self.array[self.top] = None
        
        if self.top > 0:
            self.top -= 1
        
        self.size -= 1

        return return_val
    
    def isAtCapacity(self):
        return self.size == 3

if __name__ == "__main__":
    testSetOfStack = SetOfStacks()
    testSetOfStack.push(1)
    testSetOfStack.push(2)
    testSetOfStack.push(3)
    testSetOfStack.push(4)
    print(testSetOfStack)
    testSetOfStack.pop()
    testSetOfStack.pop()
    print(testSetOfStack)