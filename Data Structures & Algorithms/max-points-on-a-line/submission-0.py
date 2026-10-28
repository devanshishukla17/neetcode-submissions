class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from math import gcd
        ans=1
        for i,(x,y) in enumerate(points):
            cnt={}
            for xx,yy in points[i+1:]:
                dx,dy=xx-x,yy-y
                g=gcd(dx,dy)
                dx,dy=dx//g,dy//g
                if dx<0 or (dx==0 and dy<0):
                    dx,dy=-dx,-dy
                key=(dx,dy)
                cnt[key]=cnt.get(key,0)+1
                ans=max(ans,cnt[key]+1)
        return ans
