"""
Chapter 2 Linked Lists
Write code to remove duplicates from an unsorted linked list. 
Follow up: How would you solve this if a temporary is not allowed.
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
