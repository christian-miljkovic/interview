"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# Functioning Solution
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False
        
        start_point_list = find_start(board, word[0])
        if len(start_point_list) > 0:
            for start_point in start_point_list: # -> (1,1) and (1,3)
                isVisited = dict()
                if dfs(board, start_point[0], start_point[1], word, isVisited):
                    return True
        
        return False
            

def find_start(board, target_letter): # target = 'S'
    result = []
    for i, row in enumerate(board): # -> 0, ['A','B','C','E']
        for j, letter in enumerate(row): # -> 0, 'A' -> 1, 'B' -> 2, 'C' -> 3,'E'
            if letter == target_letter:
                result.append((i,j)) # -> (1,0) and (1,3)
    return result

def dfs(board, i, j, word, isVisited):
    
    if len(word) == 0:
        return True
    
    if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
        return False
    
    if (i,j) in isVisited:
        return False 
    
    if board[i][j] != word[0]: 
        return False
    
    else:
        isVisited[(i,j)] = True
        result = dfs(board, i-1, j, word[1:], isVisited) or dfs(board, i, j-1, word[1:], isVisited) or dfs(board, i+1, j, word[1:], isVisited) or dfs(board, i, j+1, word[1:], isVisited)
        if not result:
            del isVisited[(i,j)]
            return False
        else:
            return True
        
        

        


# Solution not fully accurate using to learn from

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False
        
        start_point_list = find_start(board, word[0])
        if len(start_point_list) > 0:
            for start_point in start_point_list: # -> (1,1) and (1,3)
                isVisited = dict()
                curr_word = ""
                if dfs(board, start_point[0], start_point[1], word, curr_word, isVisited):
                    return True
        
        return False
            

def find_start(board, target_letter): # target = 'S'
    result = []
    for i, row in enumerate(board): # -> 0, ['A','B','C','E']
        for j, letter in enumerate(row): # -> 0, 'A' -> 1, 'B' -> 2, 'C' -> 3,'E'
            if letter == target_letter:
                result.append((i,j)) # -> (1,0) and (1,3)
    return result

def dfs(board, i, j, word, curr_word, isVisited):
    if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
        return False
    
    if (i,j) in isVisited:
        return False
    
    
    isVisited[(i,j)] = True
    new_word = curr_word + board[i][j]  
    print(new_word, curr_word, (i,j))
    
    if new_word != word[:len(new_word)]:
        del isVisited[(i,j)] 
        return False
    
    elif word == new_word:
        return True
    
    else:
        return dfs(board, i-1, j, word, new_word, isVisited) or dfs(board, i, j-1, word, new_word, isVisited) or dfs(board, i+1, j, word, new_word, isVisited) or dfs(board, i, j+1, word, new_word, isVisited)
        
        
        
      
        
        
        
        