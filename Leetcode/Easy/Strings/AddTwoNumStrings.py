"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


"""
num1 = "40"
num2 = "2"

1. Loop through nums1 converting using ord - 48 and adding to a total and multiply by 10 for each base
2. Repeat for nums2

ord() -> ascii 48-57 is 0-9
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        total = 0
        base_one = 1
        base_two = 1
        
        for num in reversed(num1):
            num_int = ord(num) - 48
            total += num_int * base_one
            base_one *= 10
        
        for num in reversed(num2):
            num_int = ord(num) - 48
            total += num_int * base_two
            base_two *= 10
        
        return str(total)
        