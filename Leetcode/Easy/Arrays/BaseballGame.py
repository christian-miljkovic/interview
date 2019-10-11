
"""
Input: list of strings 

Edge Cases:
- Empty strings
- Empty list
- stack gets popped and there is nothing there
- no item and round gets doubled -> 0
- only one item and you get '+' -> non-empty + 0
- one item with only chars not ints

Solution: use stack


Output: int -> total amount of points after all operations

"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        total = 0
        stack = collections.deque()
        
        for char in ops:
            if char[-1].isdigit():
                stack.appendleft(int(char))
                total += int(char)
            else:
                if char == 'C' and len(stack) > 0:
                    prev_round = stack.popleft()
                    total -= prev_round
                elif char == 'D' and len(stack) > 0:
                    double_round = stack[0]*2
                    total += double_round
                    stack.appendleft(double_round)
                elif char == '+':
                    if len(stack) > 1:
                        new_round = stack[1] + stack[0]
                        total += new_round
                        stack.appendleft(new_round)
                    elif len(stack) == 1:
                        new_round = stack[0]
                        total += new_round
                        stack.appendleft(new_round)
                        
        return total
                         
        