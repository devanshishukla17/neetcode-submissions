class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        st,cookie=0,0
        m,n=len(g),len(s)
        while st<m and cookie<n:
            if s[cookie]>=g[st]:
                st+=1
            cookie+=1
        return st