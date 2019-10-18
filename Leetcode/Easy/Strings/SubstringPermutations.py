# Given two strings A and B, find the starting index of all substrings
# of string A matching string B, or any permutation of string B

# a= zzzabczzabczz 
# b = abc
# return [3,8]
# "" ""

"""
Input: str a and b
Assumptions:


Idea 1: Sliding window Time Complexity: O(n) Space: O(n)

Edge cases:
- a or b empty
- if b > a no match
- a == b

Output: list of indicies that rep start of b in a
- if no indicies return empty list
"""

# Time Complexity: O(n) where n is the length of the first string
# Space Complexity: O(n) 

def substrings_in_str(A, B):
  
  if not A or not B:
    return []
    
  if A == B:
    return [0]
    
  if len(B) > len(A):
    return []
    
  return_list = []
  i = 0
  
  b_map = dict()
  for char in B:
    if char not in b_map:
      b_map[char] = 1
    else:
      b_map[char] += 1
  
  a_map = dict()
  while i < len(A):
    
    is_subtring = True
    for j in range(0,len(B)):
      if i+j < len(A):
        if A[i+j] not in b_map:
          is_subtring = False
          break
        else:
          if A[i+j] not in a_map:
            a_map[A[i+j]] = 1
          else:
            a_map[A[i+j]] += 1          
      else:
        is_subtring = False
        break
    
    if is_subtring:
      if a_map == b_map:
        return_list.append(i)
    
      
    a_map = dict()          
    i += 1
    
  
  return return_list

if __name__ == '__main__':    
    A = "zzzabczzabczz"
    B = "abc"
    C = "cd"
    D = "cd"
    E = "abcd"
    F = ""
    Z = "zz"
    perm_b = "bca"

    print(substrings_in_str(A, B))
    print(substrings_in_str(C, D))
    print(substrings_in_str(C, E))
    print(substrings_in_str(A, D))
    print(substrings_in_str(A, F))
    print(substrings_in_str(A, Z))
    print(substrings_in_str(A, perm_b))
        
