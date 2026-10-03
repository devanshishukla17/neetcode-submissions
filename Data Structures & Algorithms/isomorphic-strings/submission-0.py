class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        s1,s2={},{}
        for i in range(n):
            c1,c2=s[i],t[i]
            if ((c1 in s1 and s1[c1]!=c2) or (c2 in s2 and s2[c2]!=c1)):
                return False
            s1[c1]=c2
            s2[c2]=c1
        return True