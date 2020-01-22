
"""
Input: list of (x,y)'s 
Edge Cases:
- empty list
- just one in list

Solution #1: Sort by min distance to 0 -> Time Complexity: O(nlogn) or O(n) depending upon algorithm (quicksort vs mergesort) Space Complexity: O(nlogn) or O(1) respective algorithms.

Solution #2: Loop through each coordinate calc abs(distance) and place in a Counter object. Return most_common(k) in reverse -> Time Complexity: O(n) Space Compelxity: O(n)


Output: list of K number of (x,y)'s closest to 0

"""

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def kClosest_sort(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []
        
        if len(points) == 1:
            return points
        
        return sorted(points, key=lambda x: math.sqrt(x[0]**2+x[1]**2))[:K]





    def kClosest_Counter(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []
        
        if len(points) == 1:
            return points
        
        hash_map = collections.Counter()
        
        for point in points:
            x_y = (point[0],point[1])
            if x_y not in hash_map:
                hash_map[x_y] = distance(x_y)
        
        return_list = []
        
        for ele in hash_map.most_common()[-K:]:
            return_list.append(list(ele[0]))
        
        return return_list
        
def distance(point):
    
    return math.sqrt(point[0]**2 + point[1]**2)
        
        
        
        
        
        
        
        
        