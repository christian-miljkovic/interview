"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        look_up = dict()
        return min(min_cost_recursive(cost, 0, look_up),min_cost_recursive(cost, 1, look_up))
        
        
        
def min_cost_recursive(cost, i, look_up):
    
    if i >= len(cost):
        return 0
    
    elif len(cost) <= 2:
        return min(cost)
    
    elif i in look_up:
        return look_up[i]
    
    else:
        print(cost[i])
        look_up[i] = cost[i] + min(min_cost_recursive(cost, i+1, look_up), min_cost_recursive(cost, i+2, look_up))            
        
        return look_up[i]

def min_cost_iterative(cost):
    
    if len(cost) < 2:
        return 0
    if len(cost) < 3:
        return min(cost)
    
    look_up = dict()
    look_up[0] = cost[0]
    look_up[1] = cost[1]
    
    for i in range(2,len(cost)):
        look_up[i] = cost[i] + min(look_up[i-2], look_up[i-1])

    return min(look_up[len(cost)-1],look_up[len(cost)-2])