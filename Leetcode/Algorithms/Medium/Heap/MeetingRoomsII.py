"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

# Time Complexity: O(n*logn)
# Space Complexity: O(n)
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key = lambda x: x[0])
        min_heap = []
        min_heap.append(intervals[0][1])
        heapq.heapify(min_heap)
        
        for interval in intervals[1:]:
            if min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        
        return len(min_heap)

# This implementation did not properly use the Heap datastructure to optimally find the solution


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        heapq.heapify(intervals)        
        current_meetings = []
        max_rooms = 0
        
        while intervals:
            
            meeting_interval = heapq.heappop(intervals)
            current_meetings = check_room_availability(current_meetings, meeting_interval)
            print(current_meetings)
            max_rooms = max(max_rooms, len(current_meetings))
        
        return max_rooms
                

def check_room_availability(ongoing_meetings, new_meeting):
    
    new_start = new_meeting[0]
    new_end = new_meeting[1]
    
    # Would normally use a linked list here but for the sake of time will just use a list instead of implementing a whole LL class
    new_ongoing_meetings = []
    
    for meeting in ongoing_meetings:
        ongoing_start = meeting[0]
        ongoing_end = meeting[1]
        
        if new_start >= ongoing_end:            
            continue
        
        new_ongoing_meetings.append(meeting)
    
    new_ongoing_meetings.append(new_meeting)
    return new_ongoing_meetings
