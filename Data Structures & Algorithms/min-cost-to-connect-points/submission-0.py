class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n,node=len(points),0
        dist=[100000000] * n
        vis=[False]*n
        edges,ans=0,0
        while edges<n-1:
            vis[node]=True
            nextnode=-1
            for i in range(n):
                if vis[i]:
                    continue
                curdist=(abs(points[i][0]-points[node][0])+abs(points[i][1]-points[node][1]))
                dist[i]=min(dist[i],curdist)
                if nextnode==-1 or dist[i]<dist[nextnode]:
                    nextnode=i
            ans+=dist[nextnode]
            node=nextnode
            edges+=1
        return ans