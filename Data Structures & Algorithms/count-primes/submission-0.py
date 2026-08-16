class Solution:
    def countPrimes(self, n: int) -> int:
        a=[False]*n
        ans=0
        for i in range(2,n):
            if not a[i]:
                ans+=1
                for j in range(i*i,n,i):
                    a[j]=True
        return ans