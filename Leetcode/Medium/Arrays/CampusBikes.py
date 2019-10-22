"""
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
"""

# Time Complexity: O(n*m) where n is the len of workers and m is the len of bikes
# Space Complexity: O(n*m)

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
  
        if not workers:
            return []

        bike_taken_set = set()
        return_list = [-1] * len(workers)
        dist_list = []
  
        for i, worker in enumerate(workers):            
            for j, bike in enumerate(bikes):    
                dist_list.append((manhattan_distance(worker,bike),i,j))
        count = 0
        worker_len = len(workers)
        sorted_list = sorted(dist_list, key=lambda x: (x[0],x[1],x[2]))
        for element in sorted_list:
            if count == worker_len:
                break
            
            dist, worker_index, bike_index = element
            if return_list[worker_index] == -1 and bike_index not in bike_taken_set:
                return_list[worker_index] = bike_index
                bike_taken_set.add(bike_index)
                count += 1
                            
        return return_list


def manhattan_distance(worker,bike):
    return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        