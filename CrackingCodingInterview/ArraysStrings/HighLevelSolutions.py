"""
Chapter 1 - Strings and Arrays
These are high level solutions that I created for the rest of the practice problems in this chapter
"""

# 1.4 Palindrom Permutation
"""
Problem: Given a string, write a function to check if it is a permutation of a palindrome.
The words do not need to be dictionary words.

Example
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta" ...)

Solution Description: The function would loop through the input and hash each one of the characters, and maintain a count within
the hash_table incrementing it everytime that the same character was seen. Then loop through the hash_map keys making sure 
that each count is even, and if there is a character with an odd count that there is only one character that has an odd count - ignoring spaces.
If there are more than two odds than return False otherwise once the looping through is done return True.

Time Complexity: Loop through the string of size m inserting into hash_table, then looping through a hashtable again (should be about half of the original string)
will lead to a O(m + m/2) which comes out to O(m)
"""

# 1.5 One Away
"""
Problem: There are three types of edits that can be performed on strings: insert a character, remove a character,
 or replace a character. Given two string, write a function to check if they are one edit or zero edits away.

Exmaple:
pale, ple -> true
pale, bake -> false

Solution Description: Loop through each string and hash each character and incrementing the count within the hash_table.
Once this is done loop through the hash table and count the number of keys that have a count that is odd. If there are more than
two then return false, if there are two then if the length of both strings are the same return true otherwise false, if there is only
one odd then return true, if there are none then return true.

Time Complexity: O(m+n) where m is length of first string and n is length of second string

Optimization: Instead of looping through both seperately what you could do is loop through them at the same time,
and have two seperate methods that do the checking. Insertion/Deletion: you loop through both while incrementing two indicies.
If at one point the chars dont equal increment the oddChecker variable and increment one of the indicies (of the longer string), 
then if the chars dont equal again return false. Replacement: use this method when the lengths are equal, then check two see 
if there are more than one characters that are not equal if so return false otherwise true. This brings the time complexity 
to O(n) where n is the length of the shorter string 
"""

# 1.6 String Compression
"""
Problem: Implement a method to perform string compression using the counts of repeated characters. For example,
str aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your
method should return the original string. Assume only uppercase and lowercase letters (a-z)

Solution: Maintain a total length of original string and compressed string to make checks whether the compressed string is larger than it. 
Maintain a prev and curr pointer for the previous character and current character. Maintain a repeatedCharCount and an empty
string that you will append the information for the compressed string. Loop through the original string incrementing repeatedCharCount
by 1 for every time prev == curr, when it doesn't append prev+repeatedCharCount to compressed string reset repeatedCharCount, set prev to curr
and increment total len of compressed string variable. If total length of compressed string > original string return original
otherwise return compressed string. 

Time Complexity: O(m) where m is the length of the original string -> Revision Time complexity O(m + k^2) 
because string concatentation results in that k^2 value

Optimization: Would be to use a list instead of empty string to append a2 for example since that operation is O(1)
then ''.join(list) would give us a time complexity of O(n)
"""

# 1.7 Rotate Matrix
"""
Problem: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees.

Solution: See RotateMatrix.py
"""