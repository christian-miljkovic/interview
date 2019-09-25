"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

"""
Input: lowercase? 
Edge cases: lower and upper case, empty string, only one vowel, odd vowels

Hash map -> identifying unique elements aka vowels in string
Stack -> Two stacks that when a vowel is found adds a special char
Another stack contains all of the vowels in reverse order

"""
# Time Compelxity: O(m)
# Space Compelxity: O(m)
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        oringinal_str_stack = collections.deque()
        vowel_stack = collections.deque()
        
        for char in s:
            lower_char = char.lower()
            if lower_char == 'a' or lower_char == 'e' or lower_char == 'i' or lower_char == 'o' or lower_char == 'u':
                oringinal_str_stack.append('*')
                vowel_stack.appendleft(char)
            else:
                oringinal_str_stack.append(char)
        
        for i in range(0,len(oringinal_str_stack)):
            if oringinal_str_stack[i] == '*':
                if len(vowel_stack) > 0:
                    oringinal_str_stack[i] = vowel_stack[0]
                    vowel_stack.popleft()
        
        return ''.join(oringinal_str_stack)