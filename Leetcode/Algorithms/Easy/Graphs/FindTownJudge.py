"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if not trust:
            return 1
        
        graph = collections.defaultdict(list)
        
        for node in range(1,N+1):
            #       edges in, edges out
            graph[node] = [0,0]

        
        for node in trust:
            graph[node[0]][1] += 1
            graph[node[1]][0] += 1
        
        
        total_judges = 0
        judge = -1
        
        for key, val in graph.items():
            if val[0] == N - 1 and not val[1]:
                total_judges += 1
                judge = key
        
        if total_judges > 1:
            return -1
        
        return judge
        