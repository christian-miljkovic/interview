"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        
        row, col = click
        
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        dfs(board, click)
        return board
        
def dfs(board, click):   
    
    size_row = len(board)
    size_col = len(board[0])
    row, col = click
    if board[row][col] != 'E':
        return
    
    
    total_mines = get_adj_mines(board, click)
    
    if total_mines > 0:
        board[row][col] = str(total_mines)
        return
    else:
        board[row][col] = 'B'
        adj_squares = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for pos in adj_squares:
            if (0 <= (row + pos[0]) < size_row) and (0 <= (col + pos[1]) < size_col):
                dfs(board, (row + pos[0], col + pos[1]))
    
def get_adj_mines(board, click):
    
    size_row = len(board)
    size_col = len(board[0])
    row, col = click
    
    adj_squares = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    total_mines = 0
    
    for pos in adj_squares:
        if (0 <= (row + pos[0]) < size_row) and (0 <= (col + pos[1]) < size_col) and board[(row + pos[0])][(col + pos[1])] == 'M':
            total_mines += 1
            
    return total_mines