"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Improvement: To reduce space complexity to O(1) we could update the values to be -1 to indicate previously alive,
and then to indicate it changed from dead to alive we can place 2 in the location where again the magnitude indicates to us
the previous state so that we can use that information to make the continuous updates 
"""

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        hash_map = dict()
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                pos = (i,j)
                hash_map[pos] = is_alive(pos, board)
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                pos = (i,j)
                if hash_map[pos] == True:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

def is_alive(position, board):
    
    i, j = position
    row_size = len(board)
    col_size = len(board[0])
    
    neighbor_count = 0
    
    if i - 1 >= 0 and board[i-1][j] == 1:
        neighbor_count += 1
        
    if j - 1 >= 0 and board[i][j-1] == 1:
        neighbor_count += 1
        
    if i + 1 < row_size and board[i+1][j] == 1:
        neighbor_count += 1
        
    if j + 1 < col_size and board[i][j+1] == 1:
        neighbor_count += 1
    
    if j + 1 < col_size and i + 1 < row_size and board[i+1][j+1] == 1:
        neighbor_count += 1

    if j - 1 >= 0 and i - 1 >= 0 and board[i-1][j-1] == 1:
        neighbor_count += 1        
    
    if j + 1 < col_size and i - 1 >= 0 and board[i-1][j+1] == 1:
        neighbor_count += 1
    
    if j - 1 >= 0 and i + 1 < row_size and board[i+1][j-1] == 1:
        neighbor_count += 1
    
    
    if board[i][j] == 1:
        if neighbor_count < 2:
            return False
        elif neighbor_count > 3:
            return False
        else:
            return True                
    else:
        if neighbor_count == 3:
            return True
        else:
            return False
        
    