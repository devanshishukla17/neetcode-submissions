class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        n,m=len(word1),len(word2)
        maxi=max(n,m)
        for i in range(maxi):
            if i<n:
                ans+=word1[i]
            if i<m:
                ans+=word2[i]
        return "".join(ans)