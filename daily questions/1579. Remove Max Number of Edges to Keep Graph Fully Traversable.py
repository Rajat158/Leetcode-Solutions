'''
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
'''
class Solution:

    def dfs(self,vis,li,com,i):
        if(vis[i]):
            return 0
        vis[i]=com
        ans=1
        for j in li[i]:
            ans+=self.dfs(vis,li,com,j)
        return ans

    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        ans=0
        li=[[] for i in range(n)]
        for l in e:
            if(l[0]==3):
                li[l[1]-1].append(l[2]-1)
                li[l[2]-1].append(l[1]-1)
        vis=[0 for i in range(n)]
        com=0
        for i in range(n):
            if(vis[i]):
                continue
            else:
                com+=1
                temp=self.dfs(vis,li,com,i)
                ans+=(temp-1)
        lia=[[] for i in range(com)]
        lib=[[] for i in range(com)]
        for l in e:
            if(l[0]==1):
                a=vis[l[1]-1]-1
                b=vis[l[2]-1]-1
                if(a==b):
                    continue
                lia[a].append(b)
                lia[b].append(a)
            elif(l[0]==2):
                a=vis[l[1]-1]-1
                b=vis[l[2]-1]-1
                if(a==b):
                    continue
                lib[a].append(b)
                lib[b].append(a)
        visa=[0 for i in range(com)]
        coma=0
        comb=0
        for i in range(com):
            if(visa[i]):
                continue
            else:
                coma+=1
                if(coma>1):
                    return -1
                self.dfs(visa,lia,coma,i)
        
        visb=[0 for i in range(com)]
        for i in range(com):
            if(visb[i]):
                continue
            else:
                comb+=1
                if(comb>1):
                    return -1
                self.dfs(visb,lib,comb,i)
        if(coma>1 or comb>1):
            return -1
        ans+=(com-1)*2
        return len(e)-ans


