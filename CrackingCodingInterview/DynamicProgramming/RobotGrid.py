"""
Chapter 8 Dynamic Programming and Recursion
Problem - Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can move in two direction, right and down, but certain cells are "off limits" such that 
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
"""

def getPath(matrix, i, j, path):
    if i < 0 or j < 0:
        return    
    elif matrix[i][j] == '*':
        return 
    elif i == 0 and j == 0:
        path.append((i,j))
        return path
    else:
        pathOne = getPath(matrix, i - 1, j, path.append((i-1,j)))
        pathTwo = getPath(matrix, i, j - 1, path.append((i,j-1)))
        return min(len(pathOne), len(pathTwo))

matrix = [["","","","",'*'],
        ['*',"","",'*',""],
        ["",'*',"","",""]
        ]
path = []
print(getPath(matrix, len(matrix)-1, len(matrix[0])-1,path))