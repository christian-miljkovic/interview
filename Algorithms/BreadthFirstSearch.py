# Breadth first search alogrithm on an adjacency matrix
import random
from collections import deque

class AdjacencyMatrix:

    def __init__(self,numberOfNodes):
        self.graph = []
        for i in range(0, numberOfNodes):
            randomZeroList = [0] * (numberOfNodes)
            randomOneList = [1] * (numberOfNodes)
            randomZeroList.extend(randomOneList)
            random.shuffle(randomZeroList)

            # Prevent a vertex from being able to have an edge to itself
            randomZeroList[i] = 0

            # Splicing the lists here to have the correct side regardless of if it is even or odd
            self.graph.append(randomZeroList[:numberOfNodes])

    # Performing a traversal of the graph
    def breadthFirstTraversal(self, startNode):

        isVisited = [False] * len(self.graph)
        queue = deque()

        queue.append(self.graph[startNode])
        isVisited[startNode] = True
        
        while(queue):

            # node is a list that represents whether the current node is connected to other verticies
            node = queue.popleft()
            print(self.graph.index(node))

            for i, ele in enumerate(node):
                if(isVisited[i] == False and ele == 1):
                    queue.append(self.graph[i])
                    isVisited[i] = True
        

if __name__ == '__main__':
    adjMatrix = AdjacencyMatrix(3)
    print(adjMatrix.graph)
    adjMatrix.breadthFirstTraversal(1)