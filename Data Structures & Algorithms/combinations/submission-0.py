class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        for m in range(1<<n):
            c=[]
            for bit in range(n):
                if m&(1<<bit):
                    c.append(bit+1)
            if len(c)==k:
                ans.append(c)
        return ans