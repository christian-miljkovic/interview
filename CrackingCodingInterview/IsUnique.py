"""
Chapter 1 Array's and Strings isUnique problem
Implement an algorithm to determine if a string has all unique characters without using additional data structures.
Time Complexity: O(m*m) = O(m) since usually with two strings of different length it would be O(n*m)
Space Complexity: O(m)
Improvements: Use memoization
"""
# Use dynamic programming to find if there are any duplicates
def isUniqueWrapper(originalStr):
    if(isUnique(originalStr, originalStr, len(originalStr), len(originalStr)) > 0):
        return True
    return False

def isUnique(strOrig, strDup, i, j):
    if(i == 0 or j == 0):
        return 0
    elif(strOrig[i-1] == strDup[j-1] and i != j):
        return 1 + isUnique(strOrig, strDup, i - 1, j - 1)
    else:
        return max(isUnique(strOrig, strDup, i - 1, j), 
                    isUnique(strOrig, strDup, i, j - 1))

if __name__ == '__main__':
    testOne = 'abcdef'
    testTwo = 'abcdfa'
    testThree = ""
    print(isUniqueWrapper(testOne))
    print(isUniqueWrapper(testTwo))
    print(isUniqueWrapper(testThree))
