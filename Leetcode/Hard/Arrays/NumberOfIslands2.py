


# Failed Attempt

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        island_dict = collections.defaultdict(set)
        adj_loc = [(1,0), (0,1), (-1,0), (0,-1)]
        island_id = 0
        output_list = []
        
        
        for pos in positions:
            if not tuple(pos) in island_dict:                
                island_dict[tuple(pos)].add(island_id)
                island_id += 1
            
            for next_loc in adj_loc:
                new_row, new_col = pos[0] + next_loc[0], pos[1] + next_loc[1]
                if 0 <= new_row < m and 0 <= new_col < n:
                    if (new_row, new_col) in island_dict:
                        island_dict[tuple(pos)] = island_dict[tuple(pos)]|(island_dict[(new_row, new_col)])
                        island_dict[(new_row, new_col)] = island_dict[tuple(pos)]
            
            
            islands = island_id - max_set(island_dict) + 1
            output_list.append(islands)
            
        return output_list
            
        
        
def max_set(island_dict):
    
    max_set = 0
    for key, list_val in island_dict.items():
        max_set = max(len(list_val), max_set)
    return max_set