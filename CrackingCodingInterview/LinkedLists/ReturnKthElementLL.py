"""
Chapter 2 Linked List Questions
Problem: Return Kth to Last: Implement an algorithm to find the kth to last element of singly linked list
"""
import sys
sys.path.append('../DataStructures')
from LinkedList import LinkedList


def kToLast(head, k):
    curr = head
    kNode = curr
    while curr.nextNode != None:
        curr = curr.nextNode
        if k == 0 and kNode.nextNode != None:
            kNode = kNode.nextNode
        else:
            k -= 1

    if k > 0:
        return None

    return kNode.nodeData

if __name__ == "__main__":
    testLinkedList = LinkedList()
    testLinkedList.addNode(6)
    testLinkedList.addNode(5)
    testLinkedList.addNode(4)
    testLinkedList.addNode(3)
    testLinkedList.addNode(2)
    testLinkedList.addNode(1)
    print(testLinkedList)
    print(kToLast(testLinkedList.head, 2))
    print(kToLast(testLinkedList.head, 0))
    print(kToLast(testLinkedList.head, 7))