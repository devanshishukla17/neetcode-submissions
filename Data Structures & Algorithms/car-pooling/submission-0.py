class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans=[]
        for p,s,e in trips:
            ans.append([s,p])
            ans.append([e,-p])
        ans.sort()
        cur=0
        for point,p in ans:
            cur+=p
            if cur>capacity:
                return False
        return True