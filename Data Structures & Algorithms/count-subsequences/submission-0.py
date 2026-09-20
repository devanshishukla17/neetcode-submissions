class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[0]*(n+1)
        for i in range(1,m+1):
            l=1
            for j in range(1,n+1):
                cur=dp[j]
                r=0
                if s[i-1]==t[j-1]:
                    r=l
                nr=cur
                dp[j]=(r+nr)
                l=cur
        return dp[n]