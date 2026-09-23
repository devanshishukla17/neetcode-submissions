from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a,b,c=len(s1),len(s2),len(s3)
        if a+b<c:return False

        @lru_cache
        def dfs(i,j,k):
            if k==c:return i==a and j==b
            ans=False
            if i<a and s1[i]==s3[k]:
                ans|=dfs(i+1,j,k+1)

            if not ans and j<b and s2[j]==s3[k]:
                ans|=dfs(i,j+1,k+1)
            return ans
        return dfs(0,0,0)