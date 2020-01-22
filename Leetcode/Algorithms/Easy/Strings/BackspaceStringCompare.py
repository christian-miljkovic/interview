"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space ?
"""

"""
Algorithm: Loop through each string and add each char in a stack if # char is reached pop the top element. 
Then pop the stacks and if each char is not the same then return false otherwise true. 
Time Complexity: O(m+n) Space Complexity: O(1) since we end up with two empty stacks if we pop the element in the below example 
we do not. Another way to achieve Space Complexity O(1) would be to use two pointers and start from end of string and
skip the next char if you find a '#'

Input: lowercase a-z and '#'
Edge Cases: s = "#" or t="#" -> have to make sure not poping on empty stack

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        s_stack = process_stack(S)
        t_stack = process_stack(T)
        
        if len(s_stack) == len(t_stack):
            for i in range(0,len(s_stack)):
                if s_stack[i] != t_stack[i]:
                    return False
            
            return True
        
        return False
        
def process_stack(str_input):
    
    stack = collections.deque()
        
    for char in str_input:
        if char == "#" and len(stack) > 0:
            stack.popleft()
        elif char != "#":
            stack.appendleft(char)
    
    return stack