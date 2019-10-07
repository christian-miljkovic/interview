"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""

# Time Complexity: O(m + n) where m is the size of the sentences and n is the size of the similar pairs
# Space Complexity: O(n) where n is the size of similar pairs

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        if words1 == words2:
            return True
        if not pairs and words1 != words2:
            return False
        
        hash_map = pre_process(pairs)
        
        for index,word in enumerate(words1):
            if words1[index] == words2[index]:
                continue
            
            if word not in hash_map:
                return False
            
            similar_words = hash_map[word]
            if words2[index] not in similar_words:
                return False
            
        return True
        
        
def pre_process(pairs):
    
    hash_map = dict()
    
    for pair in pairs:
        word_one = pair[0]
        word_two = pair[1]
        
        if word_one not in hash_map:
            hash_map[word_one] = [word_two,word_one]
        else:
            hash_map[word_one].append(word_two)
            
        if word_two not in hash_map:
            hash_map[word_two] = [word_one,word_two]
        else:
            hash_map[word_two].append(word_one)
            
    return hash_map
