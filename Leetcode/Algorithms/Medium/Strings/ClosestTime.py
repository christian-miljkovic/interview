"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""


# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        split_list = time.split(':')
        num_list = ''.join(split_list)
        num_list = [int(x) for x in num_list]
        new_num_list = num_list.copy()
        new_num_list[-1] += 1
        new_num_list = adjust_time(new_num_list)
        min_diff = 0
        num_set = set(num_list)
        increment = 1
        
        while num_list != new_num_list:
            count = 0
            for num in new_num_list:
                if num in num_set:
                    count += 1
            
            if count == 4:
                min_diff = increment
                return stringify_time(new_num_list)
            
            new_num_list[-1] += 1
            increment += 1
            new_num_list = adjust_time(new_num_list)
            
            
        return stringify_time(new_num_list)

    
def stringify_time(time_list):
    str_list = [str(x) for x in time_list]
    return ''.join(str_list[:2]) + ":" + ''.join(str_list[2:])
        
def adjust_time(time):
    
    time_list = time.copy()
    
    if time_list[-1] == 10:
        time_list[-2] += 1
        time_list[-1] = 0
    
    if time_list[-2] == 6:
        time_list[-3] += 1
        time_list[-2] = 0
    
    if time_list[0] < 2:
        if time_list[1] == 10:
            time_list[1] = 0
            time_list[0] += 1
    
    else:
        if time_list[1] == 4:
            time_list[0], time_list[1] = 0, 0    
    
    return time_list
