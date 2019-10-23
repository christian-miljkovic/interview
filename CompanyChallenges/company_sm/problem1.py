"""
Shifting Strings
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getShiftedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER leftShifts
#  3. INTEGER rightShifts
#
def leftShift(text):
    firstChar = text[0]
    restOfWord = text[1:]
    return restOfWord + firstChar

def rightShift(text):
    lastChar = text[-1]
    restOfWord = text[:-1]
    return lastChar + restOfWord

def getShiftedString(s, leftShifts, rightShifts):

    if(len(s) == 1):
        return s
    
    if leftShifts != len(s):
        for i in range(0,leftShifts):
            s = leftShift(s)

    if rightShifts != len(s):
        for i in range(0,rightShifts):
            s = rightShift(s)
    
    return s