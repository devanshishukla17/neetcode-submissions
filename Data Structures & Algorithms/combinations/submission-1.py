class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def back(pos,t,temp):
            if t==0:
                ans.append(temp[:])
                return
            if pos==n+1 or t<0:
                return
            for i in range(pos,n+1):
                back(i+1,t-1,temp+[i])
        back(1,k,[])
        return ans