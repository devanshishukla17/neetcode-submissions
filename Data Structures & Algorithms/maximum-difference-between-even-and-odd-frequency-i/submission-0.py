class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        odd,even=0,len(s)
        for cnt in count.values():
            if cnt&1:
                odd=max(odd,cnt)
            else:
                even=min(even,cnt)
        return odd-even