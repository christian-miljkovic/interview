"""
Getting a Different Number
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4 

"""

"""
currMin = 0
a = [0, 1, 100,  23, 33] 


a = [22, 1, 2, 3, 4] [0 - 5]  
i =  0  1  2  3  4
output = 2

make map
{0:true}
{1:true}
{100:true}
{23:true}
{33:true}

i =  0  1  2     3   4


Sorted:
b = [0, 1, 3, 33, 100] 

output:1

1. Loop through the array once find the min
2. Look for sorted pair that has greater difference than one

for i in range length of array  #0-5

  if(i does not exist in map) return i
  
return array length  

"""

# Time Complexity: O(n)
# Space Complexity: O(n)

def get_different_number(arr):
  len_arr = len(arr)
  hash_map = dict()
  
  for num in arr:
    hash_map[num] = True
    
  for i in range(0,len_arr):
    if i not in hash_map:
      return i
  
  return len_arr
  
  
  
  