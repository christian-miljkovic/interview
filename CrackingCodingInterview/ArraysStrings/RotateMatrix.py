"""
Chapter 1
Problem - Rotate Matrix: Rotate a Matrix 90 degrees
"""

def rotateMatrix(matrix):

    size = len(matrix)

    for layer in range(size//2):

        first = layer
        last = size - layer - 1

        for i in range(first, last):

            top = matrix[layer][i]

            # left to top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # top to right
            matrix[i][-layer - 1] = top

    return matrix

if __name__== "__main__":
    testArray = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    print(rotateMatrix(testArray))
            

             