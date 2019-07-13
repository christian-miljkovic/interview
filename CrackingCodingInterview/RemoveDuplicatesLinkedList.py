"""
Chapter 2 Linked Lists
Write code to remove duplicates from an unsorted linked list. 
Follow up: How would you solve this if a temporary is not allowed.
Time Complexity: O(n)
Space Complexity: O(n)
Improvements: Could have returned the pointer to the duplicate node instead of having to find it again in the
removeNode() method. 
Follow up: Could sort the linked list using an algorithm like quickSort then see if there are two nodes with the same data values
right next to each other. This would however result in a time complexity of O(nlogn) due to the sorting but save 
space complexity by not requiring any sort of buffer therefore O(1)
"""
import sys
sys.path.append('../DataStructures')
from LinkedList import LinkedList

def removeDupe(head):
    if head == None:
        return
    data = findDupe(head)
    if(data != None):
        removeNode(head, data)


def removeNode(head, data):
    isFound = False
    prev = None
    curr = head
    while curr != None and isFound == False:
        if(curr.nodeData == data):
            isFound = True
        else:
            prev = curr
            curr = curr.nextNode

    if prev == None:
        head = None
    if isFound == True:
        prev.nextNode = curr.nextNode

def findDupe(head):
    if head == None:
        return
    hash_map = dict()
    curr = head
    while curr != None:
        if curr.nodeData in hash_map.keys():
            return curr.nodeData
        else:
            hash_map[curr.nodeData] = True
            curr = curr.nextNode

testLinkedList = LinkedList()
testLinkedList.addNode(1)
testLinkedList.addNode(5)
testLinkedList.addNode(3)
testLinkedList.addNode(6)
testLinkedList.addNode(5)
testLinkedList.addNode(4)
print(testLinkedList)
removeDupe(testLinkedList.head)
print(testLinkedList)
