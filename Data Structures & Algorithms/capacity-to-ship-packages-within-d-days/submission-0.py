class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def ship(s):
            ships,current=1,s
            for w in weights:
                if current-w < 0:
                    ships+=1
                    if ships>days:
                        return False
                    current=s
                current-=w
            return True
        while l<=r:
            s=(l+r)//2
            if ship(s):
                res=min(res,s)
                r=s-1
            else:
                l=s+1
        return res