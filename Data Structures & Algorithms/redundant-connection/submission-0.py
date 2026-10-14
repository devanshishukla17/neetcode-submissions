class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        ind=[0]*(n+1)
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            ind[u]+=1
            ind[v]+=1
        q=deque()
        for i in range(1,n+1):
            if ind[i]==1:
                q.append(i)
        while q:
            node=q.popleft()
            ind[node]-=1
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==1:
                    q.append(nei)
        for u,v in reversed(edges):
            if ind[u]==2 and ind[v]:
                return [u,v]
        return []