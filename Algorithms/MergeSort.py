# Mergesort algorithm for sorting a list
import random

def mergeSort(array, lowIndex, highIndex):

    if(len(array) > 1):
        mid = len(array)//2
        leftArray = array[lowIndex:mid]
        rightArray = array[mid:highIndex]
        print(leftArray, rightArray)
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

if __name__ == '__main__':
    unsortedTestList = random.sample(range(0,100),10)
    print(unsortedTestList)
    mergeSort(unsortedTestList, 0, len(unsortedTestList))
    print(unsortedTestList)
