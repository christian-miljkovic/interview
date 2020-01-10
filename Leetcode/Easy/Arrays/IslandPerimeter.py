"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        
        queue = collections.deque()
        total_edges = 0
        start = find_start(grid)
        pos = {(1,0), (0,1), (-1,0), (0,-1)}
        
           
        grid[start[0]][start[1]] = 2
        queue.append(start)
        
        while queue:
            
            row, col = queue.popleft()
            curr_edges = 4
            
            for x, y in pos:
                new_row = row + x
                new_col = col + y

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if grid[new_row][new_col] == 1:
                        curr_edges -= 1
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                    elif grid[new_row][new_col] == 2:
                        curr_edges -= 1
              
            total_edges += curr_edges            
            
        return total_edges
        
        
def find_start(grid):
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                return (i, j)