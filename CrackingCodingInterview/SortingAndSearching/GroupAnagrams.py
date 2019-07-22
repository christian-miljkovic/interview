"""
Chapter 10 - Sorting and Searching
Problem - Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
Time Complexity: Assuming n is length of anagram list and m is for the length of each string on average O(n*m)
This should be better than sorting the strings and then inserting into a hash table the sorted string because the sort will cost time
"""

def createAnagramTable(anagram):
    hash_table = dict()
    for char in anagram:
        hash_table[char] = True
    return hash_table

def createHashOfDictionary(dictionary):
    return hash(frozenset(dictionary.items()))

        
def sortAnagrams(anagramList):
    
    anagram_hashTable = dict()
    sorted_list = []

    for index, anagram in enumerate(anagramList):
        new_hashTable = createAnagramTable(anagram)
        newHash = createHashOfDictionary(new_hashTable)
        if newHash not in anagram_hashTable.keys():
            anagram_hashTable[newHash] = index
        else:
            sorted_list.append(anagramList[index])
            prev_index = anagram_hashTable[newHash]
            sorted_list.append(anagramList[prev_index])
    
    return sorted_list


if __name__ == "__main__":
    anagramList = ["belows","iceman","state","elbow","listen","taste","silent","elbosw","cinema","below"]
    print(sortAnagrams(anagramList))

