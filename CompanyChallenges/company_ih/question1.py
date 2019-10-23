"""
Problem: Determine if the array has a duplicate
bool -> return True or False
[3,6,7,10,3] -> True
[1,2,3] -> False
"""

def hasDuplicates(arr):

    hashMap = dict()
    for i in range(0, len(arr)):
        if(arr[i] in hashMap.keys()):
            return True
        hashMap[arr[i]] = True    
    return False


testOne = [3,6,7,10,10]
testTwo = [1,2,3]

i = 1
arr[i] = 6

