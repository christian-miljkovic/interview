"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        ticket_graph = create_graph(tickets)
        itinerary = []
        isVisited = dict()
        path = dfs(ticket_graph, "JFK", itinerary, isVisited)
        
        return path

def create_graph(tickets: List[List[str]]):
    ticket_graph = collections.OrderedDict()
    for ticket in tickets:
        ticket_graph[ticket[0]] = (ticket[1],''.join(ticket))
    return ticket_graph

def dfs(graph, curr_flight, path, isVisited):
    
    path.append(curr_flight)
    isVisited[graph[curr_flight][1]] = True
    
    if curr_flight in graph:
        next_flight = graph[curr_flight][0]
        if next_flight not in graph:
            path.append(next_flight)
        elif graph[next_flight][1] not in isVisited:
            dfs(graph, next_flight, path, isVisited)
    
    return path
        
    