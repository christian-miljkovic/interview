"""
Chapter 8 - Dynamic Programming and Recursion
Problem - Magic Index: A magic index in an array A[0..n-1] is definied to be an index such that A[i] == i.
Given a sorted array of distinct intergers, write a method to find a magic index, if one exists in array A.
Time Complexity: O(n) since we are doing 1 + T(n-1) operations where T(n-1) are the recursive calls
Improvements: A way to improve this would be instead to do a binary search on the array
"""


def getMagicIndex(matrix, i):
    if i < 0:
        return None
    elif matrix[i] == i:
        return i
    else:
        return getMagicIndex(matrix, i-1)

matrix = [-1, 1, 3]
print(getMagicIndex(matrix,len(matrix)-1))