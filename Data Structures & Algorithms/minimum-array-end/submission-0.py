class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans=x
        a,b=1,1
        while b<=n-1:
            if a&x==0:
                if b&(n-1):
                    ans = ans | a
                b=b<<1
            a=a<<1
        return ans