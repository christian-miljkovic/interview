"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
"""

# Time Compelxity: O(n)
# Space Complexity: O(1)

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        if not tree:
            return 0
        
        max_window_size = 0
        window_size = 0
        diff_index = 0
        curr_fruits = collections.deque([tree[0]])
        basket_size = 1
        i = 0
        
        while i < len(tree):
            
            if tree[i] not in curr_fruits:
                if basket_size == 2:
                    basket_size = 1
                    i = diff_index
                    max_window_size = max(max_window_size, window_size)
                    window_size = 0
                    curr_fruits.popleft()
                    continue
                
                curr_fruits.append(tree[i])
                diff_index = i
                basket_size += 1
            
            window_size += 1
            i += 1
                    
        return max(max_window_size, window_size)