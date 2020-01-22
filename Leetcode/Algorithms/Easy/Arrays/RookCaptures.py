"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        start = find_rook(board)
        total_pawns = 0
        total_pawns += check_right(start, board)
        total_pawns += check_left(start, board)
        total_pawns += check_down(start, board)
        total_pawns += check_up(start, board)
        
        return total_pawns
        
        
def check_right(start, board):
    
    row, col = start
    
    for col in range(col, 8):        
        if board[row][col] == 'p':
            return 1
        elif board[row][col] == 'B':
            return 0
        
    return 0

def check_left(start, board):
    
    row, col = start
    
    for col in range(col, -1, -1):        
        if board[row][col] == 'p':
            return 1
        elif board[row][col] == 'B':
            return 0
        
    return 0

def check_down(start, board):
    
    row, col = start
    
    for row in range(row, 8):        
        if board[row][col] == 'p':
            return 1
        elif board[row][col] == 'B':
            return 0
        
    return 0

def check_up(start, board):
    
    row, col = start
    
    for row in range(row, -1, -1):        
        if board[row][col] == 'p':
            return 1
        elif board[row][col] == 'B':
            return 0
        
    return 0
        
def find_rook(board):
    
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == 'R':
                return row, col