"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose durat
"""

"""

if no time slot reutnr []
else dur

slotsA = [[5, 50], [60, 120], [140, 210]] len = m
slotsB = [[0, 15], [60, 70]]   3, 4, .... 100 len = n
dur = 8
output: [60, 68]

O(m*n)

start: 5
end: 50
duration: 45

start: 0
end: 15
duration: 15

[10, 50]  
[0, 15]
10  0   max(10 0) ? min(10 0) ? 
start = 10 
end =  50 and 15  
duration is unknown
10 and must end at 15

double for loop until end of one of lists
see if start is within bounds of B times and if there is enough duration in A

"""

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

def meeting_planner(slotsA, slotsB, dur):
  
  result = []
  
  for i in range(0,len(slotsA)):
    startA = slotsA[i][0]
    endA = slotsA[i][1]
    for j in range(0,len(slotsB)):
      startB = slotsB[j][0]
      endB = slotsB[j][1]   
      min_time = min(endA, endB)
      max_time = max(startA, startB)
      bound = min_time - max_time
      
      if bound >= dur:
        result.append(max_time)
        result.append(max_time+dur)

  return result