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

# 1.8 Zero Matrix
"""
Problem: Write an algorithm such that if an element in an MxN matrix is 0, its entire row 
and column are set to 0.

Solution: Assuming that we are not going to set the rows and columns as we are doing the initial loop through the matrix.
First loop through the entire matrix and store all of the locations of zero's. Then create two 
seperate methods setRowToZeros and setColToZeros. Then Loop through the previously stored locations.

Time Complexity: Worst case you have all zeros in the matrix and meaning and then setRowToZeros runs in O(M)
setColToZero runs in O(N) then you will be doing O(M+N) * M*N times therefore total time complexity O(N * M^2 + M * N^2)

Optimization: During the initial loop through keep track of the rows and columns that you do not need to check since they will
eventually be set to zero. This should reduce the number of time we have to perform the set to zero operations.
"""

# 1.9 String Rotation
"""
Problem: Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2 write code to check if s2 is a rotation of s1 using only one call to isSubstring.

Example: "waterbottle" is a rotation of "erbottlewat"

Solution: Check if the strings are of the same length, if not return true. Loop through one string and hash each char 
while incrementing the count, and do the same for the second string. If there are any odd counts then return false. Lastly,
take the first and last chars of s2 concatenate them together and see if they are a substring of s1, if yes then return true otherwise false.

Time Complexity: Where m is the length of the string O(m)

Optimal Solution: s2 will always be a substring of s1+s1. Therefore concatenate s1 to itself and check if s2 is a substring
if so return true. Assuming isSubstring is O(A+B) then the total run time sould be O(m) where m is the length of the string.

"""