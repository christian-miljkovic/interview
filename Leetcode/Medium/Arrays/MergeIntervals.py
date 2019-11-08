"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

# Time Complexity: O(nlogn)
# Space Complexity: O(n) -> due to mergesort algorithm

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        
        return_list = []
        intervals = sorted(intervals)
        curr_min = intervals[0][0]
        curr_max = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= curr_min:
                curr_min = interval[0]
                if interval[1] >= curr_max:
                    curr_max = interval[1]
            elif interval[0] <= curr_max:
                if interval[1] >= curr_max:
                    curr_max = interval[1]
            else:
                return_list.append([curr_min, curr_max])
                curr_min = interval[0]
                curr_max = interval[1]
        if [curr_min, curr_max] not in return_list:
            return_list.append([curr_min, curr_max])
            
        return return_list
                    
            