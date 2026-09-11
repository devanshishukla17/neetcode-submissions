class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num=len(isConnected)
        ans=0
        def dfs(node):
            isConnected[node][node]=0
            for n in range(num):
                if node!=n and isConnected[node][n] and isConnected[n][n]:
                    dfs(n)
        for i in range(num):
            if isConnected[i][i]:
                dfs(i)
                ans+=1
        return ans