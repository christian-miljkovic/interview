"""
Chapter 1 Array's and Strings Check Permutation problem
Given two strings write a method to decide if one is a permutation of the other.
Time Complexity: O(mn)
Space Complexity: O(mn)
"""

def isPermutation(strOne, strTwo):
    hash_map = dict()
    for char in strOne:
        if(char in hash_map.keys()):
            hash_map[char] += 1
        else:
            hash_map[char] = 1

    for char in strTwo:
        if(char in hash_map.keys()):
            hash_map[char] -= 1
        else:
            hash_map[char] = -1
    
    return abs(min(hash_map.values())) == 0 and max(hash_map.values()) == 0

if __name__ == "__main__":
    strOne = 'abc'
    strTwo = 'bca'
    strThree = 'abca'
    strFour = 'ab'
    print(isPermutation(strOne, strTwo))
    print(isPermutation(strOne, strThree))
    print(isPermutation(strOne, strFour))