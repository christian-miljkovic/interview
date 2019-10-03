"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.

"""

# Time Complexity: O(n) where n is the length of costs
# Space Complexity: O(n) because you are storing n*3 values per loop

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        look_up = {
            (0,0) : costs[0][0],
            (0,1) : costs[0][1],
            (0,2) : costs[0][2]
        }
        
        for i in range(1,len(costs)):
            
            look_up[(i,0)] = costs[i][0] + min(look_up[(i-1,1)],look_up[(i-1,2)])
            look_up[(i,1)] = costs[i][1] + min(look_up[(i-1,0)],look_up[(i-1,2)])
            look_up[(i,2)] = costs[i][2] + min(look_up[(i-1,1)],look_up[(i-1,0)])
            
        
        return min(look_up[(len(costs)-1,0)],look_up[(len(costs)-1,1)],look_up[(len(costs)-1,2)])