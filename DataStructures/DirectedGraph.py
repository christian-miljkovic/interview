# Class to implemented a generic graph for tree and graph problems

class Graph:

    def __init__(self):
        self.graph = dict()
    

    def addNode(self, node, *children):
        
        if node.data not in self.graph.keys():
            self.graph[node.data] = node

        for child in children:
            if child.data not in self.graph.keys():
                self.graph[child.data] = child
            node.children.append(child)


class Node:

    def __init__(self, data):
        self.data = data
        self.children = []