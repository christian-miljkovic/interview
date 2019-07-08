# Dijkstra's Algorithm to find the shortest path
import heapq

# Creating Graph represented as Adjacency List with verticies that have edge weights
class WeightedAdjacencyList:

    def __init__(self):
        self.graph = dict()
    
    def addVertex(self,vertex, **kwargs):
        """
        @vertex: number representing a vertex node in the graph
        @kwargs: key:value pairs that represent neighborVertex:distance
        """
        neighbors = dict()
        for neighborVertex, distance in kwargs.items():
            neighbors[neighborVertex] = distance
        
        self.graph[vertex] = neighbors
    


def dijkstraPath(graph, source):

    distance = dict()
    entry_lookup = dict()
    priorityQueue = []

    # Initialize all distances to infinity
    for vertex in graph.keys():
        distance[vertex] = float('infinity')
    
    # Construct the priority queue
    distance[source] = 0
    for vertex, dist in distance.items():
        entry = [vertex, dist]
        entry_lookup[vertex] = entry
        heapq.heappush(priorityQueue, entry)
    
    while(len(priorityQueue) > 0):

        sourceVertex, sourceDist = heapq.heappop(priorityQueue)
        for neighbor, neighborDist in graph[sourceVertex].items():
            total_distance = distance[sourceVertex] + neighborDist

            # update the data structures maintaining the information about current distances 
            if(total_distance < distance[neighbor]):
                distance[neighbor] = total_distance
                entry_lookup[neighbor][1] = total_distance
        
    return distance

if __name__ == '__main__':
    weightedAdjList = WeightedAdjacencyList()
    weightedAdjList.addVertex('U',**{'V': 2, 'W': 5, 'X': 1})
    weightedAdjList.addVertex('V', **{'U': 2, 'X': 2, 'W': 3})
    weightedAdjList.addVertex('W', **{'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5})
    weightedAdjList.addVertex('X', **{'U': 1, 'V': 2, 'W': 3, 'Y': 1})
    weightedAdjList.addVertex('Y', **{'X': 1, 'W': 1, 'Z': 1})
    weightedAdjList.addVertex('Z', **{'W': 5, 'Y': 1})
    print(dijkstraPath(weightedAdjList.graph,'X'))




