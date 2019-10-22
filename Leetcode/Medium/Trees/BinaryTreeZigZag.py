"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)

# Cleaner practice version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
  
        hash_map = collections.OrderedDict()
        queue = collections.deque()
        depth = 0
        queue.append((root,depth))
  
        while queue:
   
            node, depth = queue.popleft()
    
            if depth not in hash_map:
                hash_map[depth] = []

            hash_map[depth].append(node.val)
            depth += 1
            if node.left:
                queue.append((node.left,depth))
            if node.right:
                queue.append((node.right,depth))

        return [reverse_list(node_list, index) for index,node_list in hash_map.items()]

def reverse_list(curr_list, index):
    if index%2 != 0:
        return curr_list[::-1]
    return curr_list

        


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        return_list = [[root.val]]
        queue = collections.deque()
        level = 0
        queue.append((root,level))
        
        
        while queue:
            
            node, level = queue.popleft()
            new_list = []
            
            if node.left:
                new_list.append(node.left.val)
                queue.append((node.left,level+1))
            
            if node.right:
                new_list.append(node.right.val)
                queue.append((node.right,level+1))
                
            
            if new_list:
                if level+1 == len(return_list):
                    return_list.append(new_list)
                else:
                    return_list[level+1].extend(new_list)
                    
        
        for index,depth in enumerate(return_list):
            if index % 2 == 1:
                return_list[index] = depth[::-1]
                
        return return_list

            