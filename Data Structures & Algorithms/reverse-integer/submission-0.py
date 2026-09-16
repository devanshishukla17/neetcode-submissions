class Solution:
    def reverse(self, x: int) -> int:
        num=x
        x=abs(x)
        ans=int(str(x)[::-1])
        if num<0:
            ans*=-1
        if ans<-(1<<31) or ans>(1<<31)-1:
            return 0
        return ans