"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

"""
Implement a BFS that can only continue onto the current pixel color, until 
there are no more pixels to go to

Time Complexity: O(n)
Space Complexity: O(n)

"""
class SolutionDFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        
        start = (sr, sc)
        old_color = image[sr][sc]
        
        if old_color == new_color:
            return image
        
        dfs(start, old_color, new_color, image)
        return image
        
        
        
def dfs(start, old_color, new_color, image):
    
    row, col = start
    
    if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == old_color:
        image[row][col] = new_color
        pos = {(1,0), (0,1), (-1,0), (0,-1)}
        
        for x, y in pos:
            next_pos = (row + x, col + y)
            
            dfs(next_pos, old_color, new_color, image)



class SolutionBFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        is_visited = dict()
        queue = collections.deque()
        
        original_pixel_color = image[sr][sc]
        queue.appendleft((sr,sc))
        is_visited[(sr,sc)] = True
        image[sr][sc] = newColor
        
        while len(queue) > 0:
            
            pixel_row, pixel_col = queue.popleft()
            
            if pixel_row - 1 >= 0:
                if image[pixel_row-1][pixel_col] == original_pixel_color and (pixel_row - 1,pixel_col) not in is_visited:
                    is_visited[(pixel_row - 1,pixel_col)] = True
                    queue.append((pixel_row - 1,pixel_col))
                    image[pixel_row - 1][pixel_col] = newColor

            if pixel_row + 1 < len(image):
                if image[pixel_row+1][pixel_col] == original_pixel_color and (pixel_row + 1,pixel_col) not in is_visited:
                    is_visited[(pixel_row + 1,pixel_col)] = True
                    queue.append((pixel_row + 1,pixel_col))
                    image[pixel_row + 1][pixel_col] = newColor                    
            
            if pixel_col - 1 >= 0:
                if image[pixel_row][pixel_col-1] == original_pixel_color and (pixel_row,pixel_col-1) not in is_visited:
                    is_visited[(pixel_row,pixel_col-1)] = True
                    queue.append((pixel_row,pixel_col-1))
                    image[pixel_row][pixel_col-1] = newColor
            
            if pixel_col + 1 < len(image[0]):
                if image[pixel_row][pixel_col+1] == original_pixel_color and (pixel_row,pixel_col+1) not in is_visited:
                    is_visited[(pixel_row,pixel_col+1)] = True
                    queue.append((pixel_row,pixel_col+1))
                    image[pixel_row][pixel_col+1] = newColor  
                    
        return image