"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
"""

# Time Complexity: O(nlogn+mlogm) where n and m are the size of strings s and t
# Space Complexity: O(n+m)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        s_map = dict()
        t_map = dict()

        for index, char in enumerate(s):
            if char not in s_map:
                s_map[char] = [index]
            else:
                s_map[char].append(index)

        for index, char in enumerate(t):
            if char not in t_map:
                t_map[char] = [index]
            else:
                t_map[char] = t_map[char] + [index]
        
        return sorted(s_map.values()) == sorted(t_map.values())
