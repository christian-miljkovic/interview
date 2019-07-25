"""
Chapter 10 - Sorting and Searching
Problem - Search in Rotated Array: Given a sorted array of n intergers that has been rotated an unknown number
of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.
Time Complexity: O(log(n))
Improvements could be to see which side might be ordered properly, or could have a condition after the right index
or left index to say that if one of these returns and not None then return all the way up the stack rather than doing other side
"""

def shiftedBinarySearch(array, start, end, element):
    if start < end:
        midPoint = (start + end)//2
        if array[midPoint] == element:
            return midPoint
        elif array[start] == element:
            return start
        elif array[end] == element:
            return end
        else:
            rightIndex = shiftedBinarySearch(array, midPoint + 1, end, element)
            leftIndex = shiftedBinarySearch(array, start, midPoint - 1, element)
            if rightIndex != None:
                return rightIndex
            elif leftIndex != None:
                return leftIndex
            else:
                return None

if __name__ == "__main__":
    arr = [5,6,0,2,3,4]
    print(shiftedBinarySearch(arr,0,len(arr)-1,6))