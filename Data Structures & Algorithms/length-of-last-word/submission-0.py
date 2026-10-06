class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,l=len(s)-1,0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            i-=1
            l+=1
        return l