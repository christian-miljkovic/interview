"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Improvement: Would be to only have one hash_table where you insert into the same way, but then decrement
when looping through t. This results in a Time Complexity: O(n) since you will return False if we reach a point where the second string 
is greater than the first string. Space Complexity: O(1) since the table stays constant
regardless of how large the input is
"""

"""
Inputs: lowercase alphabetical values, check if empty 

Brute Force: Double for loop checking to see if we find the same character in s
Improved:
1. Loop through s and add it to a hash_table (Counter) object
2. Loop through t and add it to a Counter object
3. Subtract s - t Counter objects -> Leads into complications because it does not display values of -1 so better checking a regular dictionary
4. If len(s_counter) > 0 return False else true 

Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hash_map = dict()
        t_hash_map = dict()
        
        for char in s:
            if char not in s_hash_map:
                s_hash_map[char] = 1
            else:
                s_hash_map[char] += 1

        for char in t:
            if char not in t_hash_map:
                t_hash_map[char] = 1
            else:
                t_hash_map[char] += 1 
        
        if len(s_hash_map) != len(t_hash_map):
            return False
        
        for key in s_hash_map:
            if key not in t_hash_map:
                return False
            elif t_hash_map[key] != s_hash_map[key]:
                return False
        
        return True
        
        
        
        
        