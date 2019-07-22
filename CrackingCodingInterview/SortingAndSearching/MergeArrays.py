"""
Chapter 10 Sorting and Searching
Problem - Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end
to hold B. Write a method to merge B into A in sorted order.
"""

def mergeArrays(a, b):
    startLen = len(a)
    i = 0
    j = 0
    while i < startLen and j < len(b):
        if a[i] < b[j]:
            a.append(a[i])
            i += 1
        elif a[i] > b[j]:
            a.append(b[j])
            j += 1
        else:
            a.append(a[i])
            a.append(b[j])
            i += 1
            j += 1
    if i < startLen:
        for x in range(i, startLen):
            a.append(a[x])
    if j < len(b):
        for x in range(j, len(b)):
            a.append(b[x])
    
    return a[startLen:]

def mergeArraysFailedAttempt(a, b):
    
    startLengthA = len(a)
    startLengthB = len(b)
    
    while startLengthA > 0 and startLengthB > 0:
        if a[0] < b[0]:
            a.append(a[0])
            a.pop()
            startLengthA -= 1
        elif a[0] > b[0]:
            a.append(b[0])
            b.pop()
            startLengthB -= 1
        else:
            a.append(a[0])
            a.append(b[0])
            a.pop()
            b.pop()
            startLengthA -= 1
            startLengthB -= 1
    if startLengthA != 0:
        for x in range(0,startLengthA):
            a.append(a[0])
            a = a[0:]
    if startLengthB != 0:
        for x in range(0,startLengthB):
            a.append(b[x])
    return a

a = [2,4,5]
b = [1,3]
print(mergeArrays(a,b))

