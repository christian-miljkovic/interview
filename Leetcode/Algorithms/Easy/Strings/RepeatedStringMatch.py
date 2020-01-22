"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

"""
Brute Force: Keep a count of how many times you do A+A and every time check if B in A+A. Time complexity: Joining strings = O(m+m) so in this case O(m) but then
checking if B is in A+A is O(m) so total is O(m^2)
"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        new_str = ""
        total_transforms = 0
        
        while len(new_str) < len(B):  
            new_str += A 
            total_transforms += 1
            if B in new_str:
                return total_transforms
            

        new_str += A

        if B in new_str:
            return total_transforms + 1
        else:
            return -1
