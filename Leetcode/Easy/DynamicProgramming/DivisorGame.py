"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

1 <= N <= 1000
"""

# You can simply return N % 2 == 0 and that will give you the correct answer, but if you wanted to follow 
# a DP paradigm the below answer solves it. 

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return divisor_game_alice(n=N, is_alice=True)
        
        
def divisor_game_alice(n, is_alice):
    print(n, is_alice)
    if (n == 1 and is_alice) or (n == 2 and not is_alice) or (n == 3 and is_alice):
        return False
    elif (n == 1 and not is_alice) or (n == 2 and is_alice) or (n == 3 and not is_alice):
        return True
    
    else:
        return divisor_game_alice(n-1, not is_alice)
    
