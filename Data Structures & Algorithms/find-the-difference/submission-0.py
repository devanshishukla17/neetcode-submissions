class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans=0
        for a in s:
            ans^=ord(a)
        for a in t:
            ans^=ord(a)
        return chr(ans)