"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

"""
Input:
string of special chars 

Edge Cases:
- duplicates
- empty str
- imporper nesting of diff special chars

Output: true or false based on rules

"""

# Time Compelexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        stack = collections.deque()
        open_chars = {'(':')', '[':']', '{':'}'}
        
        
        for char in s:
            if char in open_chars:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev_open_char = stack.pop()
                if open_chars[prev_open_char] != char:
                    return False
        if stack:
            return False
        
        return True



class Solution2:
    def isValid(self, s: str) -> bool:
        
        queue = collections.deque()
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                queue.appendleft(char)
            else:
                
                if len(queue) == 0:
                    return False
                
                open_paran = queue.popleft()
                if checkValidParan(open_paran, char, queue) == False:
                    return False
        
        if len(queue) > 0:
            return False
        else:
            return True
    
    

            
                
def checkValidParan(open_paran, checkParan, queue):

    if open_paran == '(' and checkParan == ')':
        return True
    elif open_paran == '{' and checkParan == '}':
        return True
    elif open_paran == '[' and checkParan == ']':
        return True
    else:
        return False    
