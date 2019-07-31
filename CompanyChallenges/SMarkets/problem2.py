"""
Subarrays Problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSubarrays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#
def findContinguousArrays(numbers_list):

    if len(numbers_list) == 1:
        return numbers_list

    return_list = []
    temp_list = []
    
    for j in range(1,len(numbers_list)):
        if numbers_list[j-1] == numbers_list[j] - 1:
            if numbers_list[j-1] not in temp_list:
                temp_list.append(numbers_list[j-1])
            temp_list.append(numbers_list[j])
        else:
            if len(temp_list) > 0:
                return_list.append(temp_list)
            temp_list = []
    return return_list

def getSubArrays(array, stack):
    # return_array = [[num] for num in continguous_array if num <= k]
    if len(array) > 0:
        if len(array) == 1:
            stack.append([array])
        else:
            midPoint = len(array)//2
            leftArray = array[:midPoint]
            rightArray = array[midPoint:]
            getSubArrays(leftArray, stack)
            getSubArrays(rightArray, stack)
            stack.append(array)

def getKLessThanProducts(continguous_array, k):
    passing_arrays = []
    for array in continguous_array:
        if productOfList(array) <= k:
            passing_arrays.append(array)
    
    return len(passing_arrays)

def productOfList(array):
    result = 1
    for num in array:
        result *= num
    return result

def countSubarrays(numbers, k):
    contiguous_array = findContinguousArrays(numbers)
    sub_arrays = []
    getSubArrays(contiguous_array, sub_arrays)
    return getKLessThanProducts(sub_arrays, k)