# Randomized Quick Sort algorithm on a list of integers
import random

"""
Time complexity
Worst Case: O(n^2) when at every step the partition procedure splits an n-length array into arrays of size 1 and n−1
or when the array is already sorted
Expected Case: O(nlogn) since you have to at least go through every value once, but the swap since we are breaking the array
into sub-arrays 
"""

def quickSort(unsortedList, lowIndex, highIndex):

    if(lowIndex < highIndex):
        partion = randomizedPartion(unsortedList, lowIndex, highIndex)
        quickSort(unsortedList, lowIndex, partion - 1)
        quickSort(unsortedList, partion + 1, highIndex)

def lomutoPartion(unsortedList, lowIndex, highIndex):
    pivot = unsortedList[highIndex]
    i = lowIndex
    for j in range(lowIndex, highIndex):
        if(unsortedList[j] <= pivot):
            swap(unsortedList, i, j)
            i += 1
    swap(unsortedList, i, highIndex)
    return i

def randomizedPartion(unsortedList, lowIndex, highIndex):
    partion = random.randint(lowIndex,highIndex)
    swap(unsortedList, partion, highIndex)
    return lomutoPartion(unsortedList, lowIndex, highIndex)

def swap(listToSwap, firstIndex, secondIndex):
    tempValue = listToSwap[firstIndex]
    listToSwap[firstIndex] = listToSwap[secondIndex]
    listToSwap[secondIndex] = tempValue

if __name__ == '__main__':
    unsortedTestList = random.sample(range(0,100),10)
    print(unsortedTestList)
    quickSort(unsortedTestList, 0, len(unsortedTestList) - 1)
    print(unsortedTestList)