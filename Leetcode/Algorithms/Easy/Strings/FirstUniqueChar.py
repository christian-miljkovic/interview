

"""
Input: string (all lower case)
Edge Cases:
- empty string
- all non-repeating
- all repeating -> return -1
- non-alphabetical characters in str

Solution #1: Loop through string and add each char to a hash_map with (total,position) then return the least common -> Time Complexity: O(n) Space Complexity: O(n)

Solution #2: Nested for loop if the inner for loop ends and there and no s[i] == s[j] then return i. Time Compelxity: O(n^2) Space Complexity: O(1)

Output: index of first non-repeating letter 

"""
# Time Complexity: O(n)
# Space Complexity: O(n) 
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        
        hash_map = collections.Counter()
        
        for index, char in enumerate(s):
            if char not in hash_map:
                hash_map[char] = [1,index]
            else:
                hash_map[char][0] += 1
        
        least_common_char = hash_map.most_common()[-1]
        
        if least_common_char[1][0] > 1:
            return -1
        
        return least_common_char[1][1]
