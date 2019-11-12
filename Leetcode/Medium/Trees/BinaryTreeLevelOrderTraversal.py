"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

"""
Input: root -> binary NOT BST
Edge Cases:
- none root
- unablanced tree
- gap between nodes


Idea: 
- get max_depth -> to create all lists
- BFS
- keep track of the level and then add to the corresponding list

Output: list of lists -> depicting level order BST traversal
"""
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        depth = get_max_depth(root)
        return_list = [[] for _ in range(depth)]

        queue = collections.deque()
        queue.append((root,0))

        while queue:
            
            node, level = queue.popleft()
            return_list[level].append(node.val)
            
            if node.left:
                queue.append((node.left,level + 1))
            if node.right:
                queue.append((node.right,level + 1))
                
        return return_list

def get_max_depth(root):
    
    if not root:
        return 0
    else:
        return 1 +  max(get_max_depth(root.left), get_max_depth(root.right))
        