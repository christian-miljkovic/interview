"""
Chapter 2 Linked List Problems
Problem -  Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e. any node but the first
and last node, not neccesarily the exact middle) of a singly linked list, given only access to that node
"""
import sys
sys.path.append('../../DataStructures')
from LinkedList import LinkedList

def removeMiddleNode(head):
    curr = head
    prev = None
    mid = getMiddle(head)
    while mid > 0 and curr.nextNode != None:
        prev = curr
        curr = curr.nextNode
        mid -= 1
    
    if prev != None and curr != None:
        prev.nextNode = curr.nextNode

def getMiddle(head):
    count = 0
    curr = head
    while curr.nextNode != None:
        count += 1
        curr = curr.nextNode
    return count/2

if __name__ == "__main__":
    testLinkedList = LinkedList()
    testLinkedList.addNode('f')
    testLinkedList.addNode('e')
    testLinkedList.addNode('d')
    testLinkedList.addNode('c')
    testLinkedList.addNode('b')
    testLinkedList.addNode('a')
    
    
    print(testLinkedList)
    removeMiddleNode(testLinkedList.head)
    print(testLinkedList)