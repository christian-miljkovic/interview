"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_list,fresh_set = pre_process(grid)
        new_rotten = make_all_rotten(grid, rotten_list, fresh_set)
        minutes = 0
        
        while new_rotten:
            new_rotten = make_all_rotten(grid, new_rotten, fresh_set)
            minutes += 1
        
        if len(fresh_set) > 0:
            return -1
        else:
            return minutes
        
        
def pre_process(grid):
    
    rotten_list = []
    fresh_set = set()
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == 2:
                rotten_list.append((i,j))
            elif grid[i][j] == 1:
                fresh_set.add((i,j))
    
    return rotten_list,fresh_set

def make_all_rotten(grid, rotten_list, fresh_set):
        
    new_rotten = []
    
    for position in rotten_list:
        new_rotten.extend(make_surrounding_rotten(grid, position, fresh_set))
        
    return new_rotten
    
    
def make_surrounding_rotten(grid, location, fresh_set):
    
    row, col = location
    new_rotten_list = []
    
    if row - 1 >= 0 and grid[row-1][col] == 1:
        grid[row-1][col] = 2
        fresh_set.remove((row-1,col))
        new_rotten_list.append((row-1,col))
        
        
    if row + 1 < len(grid) and grid[row+1][col] == 1:
        grid[row+1][col] = 2
        fresh_set.remove((row+1,col))
        new_rotten_list.append((row+1,col))
        
        
    if col - 1 >= 0 and grid[row][col-1] == 1:
        grid[row][col-1] = 2
        fresh_set.remove((row,col-1))
        new_rotten_list.append((row,col-1))
        
    
    if col + 1 < len(grid[row]) and grid[row][col+1] == 1:
        grid[row][col+1] = 2
        fresh_set.remove((row,col+1))
        new_rotten_list.append((row,col+1))
        
        
    return new_rotten_list
    
    
    