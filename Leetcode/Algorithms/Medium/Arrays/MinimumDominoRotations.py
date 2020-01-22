"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

# Time Complexity: O(n) where n is the length of the lists
# Space Complexity: O(1)

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        swap_a = check_one_row(A,B)
        swap_b = check_one_row(B,A)
        
        if swap_a == swap_b and swap_a == -1:
            return -1
        elif swap_a == -1:
            return swap_b
        elif swap_b == -1:
            return swap_a
        else:
            return min(swap_a, swap_b)

    
    
def check_one_row(A,B):
    min_swaps = float('inf')
    is_filled = False

    for num in range(1,7):
        curr_swaps = 0
        correct_nums = 0
        for i in range(len(A)):
            if A[i] != num and B[i] == num:
                curr_swaps += 1
                correct_nums += 1
            elif A[i] == num:
                correct_nums += 1

        if correct_nums == len(A):
            min_swaps = min(min_swaps, curr_swaps)
            is_filled = True

    if is_filled:
        return min_swaps
    return -1