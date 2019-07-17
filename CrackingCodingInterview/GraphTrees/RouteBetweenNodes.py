"""
Chapter 4 - Trees and Graphs 
Problem - Route Between Nodes: Given a directed graph, design an algorithm to find out 
where there is a route between two nodes.
"""
import sys
sys.path.append('../../DataStructures')
from DirectedGraph import Graph, Node
from collections import deque

def isRoute(graph, source, target):
    isVisited = dict()
    sourceNode = graph[source.data]
    targetNode = graph[target.data]

    isVisited[sourceNode] = True
    queue = deque()
    queue.appendleft(sourceNode)

    while len(queue) != 0:
        node = queue.popleft()
        for child in node.children:
            if child.data == targetNode.data:
                return True
            if child not in isVisited.keys():
                isVisited[child] = True
                queue.append(child)
    
    return False

if __name__ == "__main__":
    testGraph = Graph()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    testGraph.addNode(n1, n2, n3)
    testGraph.addNode(n3, n4)
    testGraph.addNode(n5)
    print(isRoute(testGraph.graph, n1, n4))
    print(isRoute(testGraph.graph, n1, n5))