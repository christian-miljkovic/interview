"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

"""
Input: alpha numeric string
Edge Cases:
- empty string
- all uppercase 
- all lowercase
- all nums 


Idea 1: Backtracking -> due to placing calls on the stack Space Complexity: O(n^2) Time Complexity: O(n^2) because for every char you change you will do so for all the others per iteration.

Output: list of strings that represent permutations of just alphanumeric values

"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []
        
        return dfs(S, path=[])
        
        
def dfs(string, path):
    
    if string not in path:
        
        path.append(string)        
        string_list = list(string)
        
        for index, char in enumerate(string_list):
            
            if char.isalpha():
                new_char = make_opposite_case(char)
                string_list[index] = new_char
                new_string = ''.join(string_list)

                dfs(new_string, path)
                string_list[index] = char
    
    return path
        
        
def make_opposite_case(char):
    
    if char.islower():
        return char.upper()
    else:
        return char.lower()