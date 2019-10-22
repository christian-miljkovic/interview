"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""



class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        
        bolded_list = [""]*len(s)
        
        
        for word in dict:
            # TC: O(len(word) * O(n*m))
            sub_loc_list = find_substring_loc(word, s)
            # + TC: O(m*n)
            for index in sub_loc_list:
                list_word = list(word)                
                for j,char in enumerate(list_word):
                    bolded_list[index+j] = char
        
        return_list = []
        open_bracket = False
        for i in range(len(bolded_list)):
            
            if open_bracket: 
                if bolded_list[i] != '':
                    return_list.append(bolded_list[i])
                else:
                    open_bracket = False
                    return_list.append('</b>')
                    return_list.append(s[i])
            else:        
                if bolded_list[i] == '':
                    return_list.append(s[i])
            
                else:
                    open_bracket = True
                    return_list.append('<b>')
                    return_list.append(bolded_list[i])
        
        if open_bracket:
            return_list.append('</b>')            
        
        return ''.join(return_list)   

# Time Complexity: O(n*m) where n is len of substring and m is len of string
# Space Complexity: O(m) 
def find_substring_loc(sub_string, string):
    
    return_list = []
    len_string = len(string)
    try:
        index = string.index(sub_string)
    except:
        index = -1
    
    while index != -1:
        return_list.append(index)
        if index+1 >= len_string:
            break
        
        try:
            index = string.index(sub_string,index+1)            
        except:
            index = -1
        
    return return_list