"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

# Time Complexity: O(5*logn) -> O(logn) because if you look at how many times 
# you do heappush and heappop when adding you only do logn operation 5 times since
# inserting and popping from a heap is logn
# Space Complexity: O(n)

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = [] # max_heap
        self.right_heap = [] # min_heap
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.left_heap, num * -1)
        self.balance_heaps()
        
        
    def balance_heaps(self):        

        val = heapq.heappop(self.left_heap)
        heapq.heappush(self.right_heap, val * -1)
        
        if len(self.left_heap) + 1 == len(self.right_heap):
            val = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, val * -1)

            
    def findMedian(self) -> float:
        
        total_len = len(self.left_heap) + len(self.right_heap)
        
        if total_len % 2 == 1:
            if not self.left_heap:
                return float(self.right_heap[0])
            return float(self.left_heap[0] * -1)
        else:
            median = ((self.left_heap[0] * -1) + self.right_heap[0])/2
            return float(median)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()