class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        ans=3**(n//3)
        if n%3==1:
            return (ans//3)*4
        return ans*max(1,(n%3))