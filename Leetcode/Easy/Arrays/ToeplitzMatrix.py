"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Time Complexity: O(m*n)
        # Space Complexity: O(1)
        
        
        if not matrix:
            return False
        
        for i in range(0,len(matrix[0])-1):
            val = matrix[0][i]
            if not move_diagonal(matrix, val, (0,i)):
                return False
        
        for i in range(1,len(matrix)-1):
            val = matrix[i][0]
            if not move_diagonal(matrix, val, (i,0)):
                return False
        
        return True

def move_diagonal(matrix, val, start):
    
    row_len = len(matrix)
    col_len = len(matrix[0])
    i, j = start
    
    while i < row_len and j < col_len:
            
        if matrix[i][j] != val:
            return False

        i += 1
        j += 1
        
    return True
            