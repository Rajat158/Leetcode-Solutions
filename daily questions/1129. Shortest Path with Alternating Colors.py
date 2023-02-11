'''
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
'''
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """

        adj = collections.defaultdict(list)

        for s,d in redEdges:
            adj[s].append((d, 0)) 
        for s,d in blueEdges:
            adj[s].append((d, 1)) 

        ans = [-1]*n
        ans[0] = 0
        v = [[False, False] for _ in range(n)]
        v[0][0] = v[0][1] = True
            
        q = deque()
        q.append((0,0,0))
        q.append((0,0,1))
        
        while q:
            node,steps,c = q.popleft()
            for nei, col in adj[node]:
                if (col != c) and (v[nei][col] == False):
                    if ans[nei] == -1:
                        ans[nei] = steps+1
                    v[nei][col] = True
                    q.append((nei, steps+1, col))

        return ans
