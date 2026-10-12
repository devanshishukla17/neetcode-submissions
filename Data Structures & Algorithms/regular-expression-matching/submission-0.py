class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[False]*(n+1)
        dp[n]=True
        for i in range(m,-1,-1):
            dp1=dp[n]
            dp[n]=(i==m)
            for j in range(n-1,-1,-1):
                match=i<m and (s[i]==p[j] or p[j]==".")
                ans=False
                if (j+1)<n and p[j+1]=="*":
                    ans=dp[j+2]
                    if match:
                        ans |= dp[j]
                elif match:
                    ans=dp1
                dp[j],dp1=ans,dp[j]
        return dp[0]