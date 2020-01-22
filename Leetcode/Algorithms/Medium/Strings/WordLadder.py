"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

# Naive Solution that Time out exceeds
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        isVisited = [False] * len(wordList)
        curr_transformations = 1
        curr_word = beginWord
        transformations = collections.Counter()
        
        
        
        while curr_word != endWord:
            for i in range(0,len(curr_word)):
                for letter in range(97,123):
                    temp_str = curr_word[:i] + str(letter) + curr_word[i+1:]
                    if temp_str in wordList:
                        transformations[temp_str] = curr_transformations
            curr_transformations += 1
        
        return transformations.most_common()[-1][1]
            