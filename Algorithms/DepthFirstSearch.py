# Depth first search of a graph represented as Adjacency List

class AdjacencyList:

    def __init__(self):
        self.graph = dict()
    

    def addNode(self, vertex, *edges):
        listOfEdges = []
        for edge in edges:
            listOfEdges.append(edge)
        
        self.graph[vertex] = listOfEdges
    

    def depthFirstTraversal(self, vertexNumber, isVisited):
        
        if(vertexNumber in isVisited):
            return
        else:
            isVisited.append(vertexNumber)

        # If the vertex number doesn't exist in the graph then we know it is a leaf vertex and we still print
        print(vertexNumber)
        if(vertexNumber not in self.graph.keys()):
            return 
        
        listOfEdges = self.graph[vertexNumber]

        for child in listOfEdges:
            self.depthFirstTraversal(child,isVisited)

if __name__ == "__main__":
    adjList = AdjacencyList()
    adjList.addNode(0,4,7,6)
    adjList.addNode(4,2,1)
    adjList.addNode(7,8,5)
    adjList.addNode(6,3)
    adjList.addNode(3,8)
    adjList.depthFirstTraversal(0,[])