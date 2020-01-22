"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        is_visited = collections.defaultdict(dict) # index, word
        return dfs(s, wordDict, 0, is_visited)
        
def dfs(word, word_list, start_index, is_visited):
    
    if not word:
        return True
    
    next_words = get_next_words(word, word_list)
    if not next_words:
        return False
    
    else:
        
        for next_word in next_words:
            if start_index in is_visited and next_word in is_visited[start_index]:
                if is_visited[start_index][next_word]:
                    return True
                continue
            new_index = len(next_word)
            if word[:new_index] == next_word:
                is_visited[start_index][next_word] = dfs(word[new_index:], word_list, new_index, is_visited)
            else:
                is_visited[start_index][next_word] = False
                
            if is_visited[start_index][next_word]:
                return True
        
        return False
    
    
def get_next_words(word, word_list):
    
    output = []
    for dict_word in word_list:
        if word[0] == dict_word[0] and len(word) >= len(dict_word):
            output.append(dict_word)
        
    return output