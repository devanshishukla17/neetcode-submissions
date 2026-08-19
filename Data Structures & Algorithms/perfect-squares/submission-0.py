class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        cnt=1
        while cnt*cnt<=n:
            sq=cnt*cnt
            for i in range(sq,n+1):
                dp[i]=min(dp[i-sq]+1,dp[i])
            cnt+=1
        return dp[n]