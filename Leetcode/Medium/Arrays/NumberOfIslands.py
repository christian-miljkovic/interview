"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""

"""
Input: 2D array 
Assume: 
- Horizontally attached and vertically attached land == island
- One piece of land surrounded also counts
- NOT NxN dimensions

Edge Cases:
- empty grid
- grid only with one row
- grid only with one col
- no islands
- all islands

Solution #1: loop through the entire grid and as soon as you hit a 1 see if it has been visited (marked as 2), if not then BFS from it marking all 1's in path as visited. THEN increment island count by 1.


Output: island count -> int

"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        island_count = 0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j] == "1":
                    island_count += mark_islands(grid,(i,j))
        
        return island_count

def mark_islands(grid,start):
    
    row, col = start
    
    queue = collections.deque()
    queue.appendleft(start)
    
    while queue:
          
        pop_node = queue.popleft()
        row, col = pop_node
        
        if grid[row][col] == "1":
                        
            grid[row][col] = "2"            
            
            if row-1 >= 0 and grid[row-1][col] == "1":
                queue.append((row-1,col))
            
            if row + 1 < len(grid) and grid[row+1][col] == "1":
                queue.append((row+1,col))
                
            if col-1 >= 0 and grid[row][col-1] == "1":
                queue.append((row,col-1))
                
            if col+1 < len(grid[0]) and grid[row][col+1] == "1":
                queue.append((row,col+1))
        
        
        
    return 1
        