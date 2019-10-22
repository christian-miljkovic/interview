

# Approach that solves 35/36 test cases using a sliding window
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_map = dict()
        for word in wordDict:
            word_map[word] = True
        
        
        s_rev = s[::-1]
        count_regular = sliding_window(s, word_map, False)
        count_reversed = sliding_window(s_rev, word_map, True)
        print(len(s),count_regular,count_reversed)
        if count_regular == len(s) or count_reversed == len(s):
            return True
        return False


def sliding_window(s, word_map, is_reversed):

    i = count = 0
    for j in range(len(s)):
        if is_reversed:
            if s[j:][::-1] in word_map:
                count += len(s) - j
            elif s[i:j+1][::-1] in word_map:
                count += (j+1) - i
                i = j+1 
        else:
            if s[j:] in word_map:
                count += len(s) - j
            elif s[i:j+1] in word_map:
                count += (j+1) - i
                i = j+1   
        
        if count == len(s):
            break
    return count

        