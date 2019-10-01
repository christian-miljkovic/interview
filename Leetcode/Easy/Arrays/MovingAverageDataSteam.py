"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""

class MovingAverage:

    # Time Complexity: O(1)
    # Space Complexity: O(1) since we are only storing a list of len == size
    
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.total = 0
        self.window = collections.deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.total += val
            self.window.append(val)
            return self.total/len(self.window)
        else:
            self.total += val
            self.window.append(val)
            self.total -= self.window[0]
            self.window.popleft()
            return self.total/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)