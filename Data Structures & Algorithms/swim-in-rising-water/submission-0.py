class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        vis=set()
        minh=[[grid[0][0],0,0]]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        vis.add((0,0))
        while minh:
            t,r,c=heapq.heappop(minh)
            if r==n-1 and c==n-1:
                return t
            for dr,dc in directions:
                neir,neic=r+dr,c+dc
                if (neir<0 or neic<0 or neir==n or neic==n or (neir,neic) in vis):
                    continue
                vis.add((neir,neic))
                heapq.heappush(minh,[max(t,grid[neir][neic]),neir,neic])