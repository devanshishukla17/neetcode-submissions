class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    ans+=4
                    if r and grid[r-1][c]:
                        ans-=2
                    if c and grid[r][c-1]==1:
                        ans-=2
        return ans