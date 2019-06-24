# Class for implementing BinaryHeap with the min at top 

class BinaryHeap:

    def __init__(self,startingList):
        # Instantiated heap with one empty value because the first one we will keep empty
        # for ease of implementation when it comes to calculating left or right child
        self.heap = [None]
        if(startingList != None and startingList != []):
            for num in startingList:
                self.heap.append(num)

    def insert(self, newValue):
        if(newValue == None):
            return   
        self.heap.append(newValue)
        newValueIndex = len(self.heap) - 1
        while(self.isSwapable(newValueIndex)):
            self.swap(newValueIndex//2, newValueIndex)
            newValueIndex = newValueIndex//2
            

    def swap(self, parentIndex, childIndex):
        tempParent = self.heap[parentIndex]
        self.heap[parentIndex] = self.heap[childIndex]
        self.heap[childIndex] = tempParent
    
    def isSwapable(self, childIndex):
        if(childIndex <= 1):
            return False
        elif(self.heap[childIndex//2] <= self.heap[childIndex]):
            return False
        else:
            return True

testList = [10,13,15,27,38,50]
testBHeap = BinaryHeap(testList)
print(testBHeap.heap)
testBHeap.insert(12)
print(testBHeap.heap)
