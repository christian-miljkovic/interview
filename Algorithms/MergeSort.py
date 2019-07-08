"""
Mergesort algorithm for sorting a list
Time Complexity: O(nlogn)
Space Complexity: O(n) because we are essentially creating a new list for every item at the end of the recusrive call/stack
"""

import random

def mergeSort(arrayToBeSorted):

    if(len(arrayToBeSorted)>1):

        midPoint = len(arrayToBeSorted)//2
        leftArray = arrayToBeSorted[:midPoint]
        rightArray = arrayToBeSorted[midPoint:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        # these indicies are used for the two arrays being merged
        i = 0
        j = 0

        # this index is used for the new array
        k = 0

        while(i < len(leftArray) and j < len(rightArray)):
            if(leftArray[i] <= rightArray[j]):
                arrayToBeSorted[k] = leftArray[i]
                i += 1
            else:
                arrayToBeSorted[k] = rightArray[j]
                j += 1
            k += 1
        
        # check to make sure no elements were left
        while(i < len(leftArray)):
            arrayToBeSorted[k] = leftArray[i]
            i += 1
            k += 1
        while(j < len(rightArray)):
            arrayToBeSorted[k] += rightArray[j]
            j += 1
            k += 1

if __name__ == '__main__':
    unsortedTestList = random.sample(range(0,100),10)
    print(unsortedTestList)
    mergeSort(unsortedTestList)
    print(unsortedTestList)


"""
Keeping previous attempt in order to understand why/how I implemented this incorrectly

def mergeSort(array, lowIndex, highIndex):

    if(len(array) > 1):
        mid = len(array)//2
        leftArray = array[:mid]
        rightArray = array[mid:]
        arrayOne = mergeSort(leftArray, lowIndex, mid)
        arrayTwo = mergeSort(rightArray, mid, highIndex)
        return mergeArrays(arrayOne, arrayTwo)
    else:
        return array

def mergeArrays(arrayOne, arrayTwo):
    
    mergedArray = []
    indexOne = 0
    indexTwo = 0

    while(indexOne < len(arrayOne) and indexTwo < len(arrayTwo)):
        if(arrayOne[indexOne] < arrayTwo[indexTwo]):
            mergedArray.append(arrayOne[indexOne])
            indexOne += 1

        else:
            mergedArray.append(arrayTwo[indexTwo])
            indexTwo += 1
    
    return mergedArray
"""
