"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        
        curr_str = ''
        curr_num = 0
        stack = []
        wait_time = 0
        
        for index, char in enumerate(s):
            if wait_time <= 0:
            
                if char == '[':
                    stack.append(curr_num)
                    stack.append(curr_str)
                    curr_str = ''
                    curr_num = 0
                elif char == ']':
                    prev_str = stack.pop()
                    prev_num = stack.pop()
                    curr_str = prev_str + curr_str*prev_num

                elif char.isnumeric():
                    curr_num, wait_time = get_full_int(s, index)

                else:
                    curr_str += char
            
            wait_time -= 1
            
        return curr_str
    
def get_full_int(string, index):
    full_int_str = ''
    count = 0
    
    while string[index].isnumeric():
        full_int_str += string[index]
        index += 1
        count += 1
    
    return int(full_int_str), count
    