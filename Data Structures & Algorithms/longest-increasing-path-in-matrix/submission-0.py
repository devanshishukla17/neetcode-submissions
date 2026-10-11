class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp={}
        def dfs(r,c,preval):
            if (r<0 or r==rows or c<0 or c==cols or matrix[r][c]<=preval):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            ans=1
            ans=max(ans,1+dfs(r+1,c,matrix[r][c]))
            ans=max(ans,1+dfs(r-1,c,matrix[r][c]))
            ans=max(ans,1+dfs(r,c+1,matrix[r][c]))
            ans=max(ans,1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c)]=ans
            return ans
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        return max(dp.values())