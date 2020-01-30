"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""

# Time Complexity: O(2n) -> O(n)
# Space Complexity: O(1)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        
        for index, date_str in enumerate(timePoints):
            timePoints[index] = date_toInt(date_str)
        
        sorted_time_points = sorted(timePoints)
        sorted_time_points.extend([x + 1440 for x in sorted_time_points])
        
        min_diff = sorted_time_points[-1] - sorted_time_points[0]
        
        for i in range(1, len(sorted_time_points)):
            min_diff = min(min_diff, sorted_time_points[i] - sorted_time_points[i - 1])
        
        return min_diff
        
        
def date_toInt(date_str):
    
    hours, minutes = date_str.split(":")
    return int(hours)*60 + int(minutes)