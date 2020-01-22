"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

"""


class Trie(object):
    
    def __init__(self):
        self.trie = dict()
        self.end = False
        
    def add_word(self, word):
        
        temp = self
        
        for char in word:
            if char not in temp.trie:
                temp.trie[char] = Trie()
            temp = temp.trie[char]
        
        temp.end = True
        
    
    def find_longest_word(self, word):
        
        temp = self
        word_len = 0
         
        for char in word:     

            if char not in temp.trie or not temp.trie[char].end:
                break
            
            word_len += 1
            temp = temp.trie[char]
            
        
        return word_len
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        longest_words = []
        longest_length = 0
        
        for word in words:
            trie.add_word(word)
        
        for word in words:
            word_len = trie.find_longest_word(word)
            
            if word_len > longest_length:
                longest_words = []
                longest_words.append(word)
                longest_length = word_len
                
            elif word_len == longest_length:
                longest_words.append(word)
                
        return sorted(longest_words)[0]
                
                
        
        
        
        
        
        
        
        