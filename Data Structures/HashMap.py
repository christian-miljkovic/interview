# Implementation of a hash map
import collections

class HashMap:

    def __init__(self,size):
        self.map = [None] * size 
        self.size = size
        for i in range(0, size):
            newDoubleEndedQueue = collections.deque()
            self.map[i] = newDoubleEndedQueue
    
    def hash(self,string):
        totalAsciiInt = 0
        for char in string:
            totalAsciiInt += ord(char)
        return totalAsciiInt % self.size
    
    # Hash maps are allowed to store None values
    def insert(self,string):
        index = self.hash(string)
        self.map[index].append(string)

    def delete(self,string):
        index = self.hash(string)
        self.map[index].remove(string)
    
    def toString(self):
        # Representing it as a list since it easier to print
        hashList = []
        for queue in self.map:
            hashList.append(queue)
        return hashList

testHashMap = HashMap(4)
print(testHashMap.toString())
testHashMap.insert('hello')
print(testHashMap.toString())
testHashMap.insert('worldz')
print(testHashMap.toString())
testHashMap.delete('hello')
print(testHashMap.toString())