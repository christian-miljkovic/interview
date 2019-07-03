# Topological sort using Tarjan's Algorithm
from DepthFirstSearch import AdjacencyList

def topologicalSort(graph, vertexNumber, isVisited, stack):
    """
    @graph: an adjacency list representing the current
    @vertex: vertex where we want to start the topological sort from
    @isVisited: list that determines if the vertex has already been visited
    @stack: list that represents a stack where we will place a vertex once it is processed
    """

    if(vertexNumber in isVisited):
        return
    # pre-process the vertex
    isVisited.append(vertexNumber)

    # Check for when we have a leaf with no outgoing edges
    if(vertexNumber not in graph.keys()):
        return

    # graph represents an adjacency list (implemented with dict in python) where the vertex number is the key
    # to the list of children
    for child in graph[vertexNumber]:
        topologicalSort(graph,child,isVisited,stack)

    stack.append(vertexNumber)
    return stack



if __name__ == '__main__':
    adjList = AdjacencyList()
    adjList.addNode(0,1,2)
    adjList.addNode(1,2)
    adjList.addNode(2,0,3)
    adjList.addNode(3,3)
    print(topologicalSort(adjList.graph,0,[],[]))
