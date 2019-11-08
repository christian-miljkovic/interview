"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

"""
Input: 2D array
Edge Cases:
- we are not given nxn but nxm


Idea 1: Backtracking starting from mid_point

Output: true or false if the target exists

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        x = len(matrix) // 2
        y = len(matrix[0]) // 2
        
        return back_track(matrix, (x, y), target, is_visited=dict())
        
def back_track(matrix, source, target, is_visited):
    x, y = source
    
    if (x >= len(matrix) or x < 0) or (y >= len(matrix[x]) or y < 0):
        return False
    
    elif source in is_visited:
        return False
        
    elif matrix[x][y] == target:
        return True
    
    else:
        is_visited[source] = True
        
        if target > matrix[x][y]:
            return back_track(matrix, (x + 1, y), target, is_visited) or back_track(matrix, (x, y + 1), target, is_visited)
        else:
            return back_track(matrix, (x -1, y), target, is_visited) or back_track(matrix, (x, y - 1), target, is_visited)
    
    