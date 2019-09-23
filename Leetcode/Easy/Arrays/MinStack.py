"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

# Be aware of when the stack has values then returns to len == 0 because then you have to reset the curr_min val

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque()
        self.curr_min = None

    def push(self, x: int) -> None:
        if self.curr_min == None:
            self.curr_min = x
        
        self.stack.appendleft((x,self.curr_min))
        
        if x < self.curr_min:
            self.curr_min = x

    def pop(self) -> None:
        if len(self.stack) > 0:
            val, prev_min = self.stack.popleft()
            if val == self.curr_min:
                self.curr_min = prev_min
            
            if len(self.stack) == 0:
                self.curr_min = None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[0][0]

    def getMin(self) -> int:
        if self.curr_min != None:
            return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()