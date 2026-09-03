class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        l,ans=0,0
        n=len(s)
        for i in range(n):
            while s[i] in char:
                char.remove(s[l])
                l+=1
            char.add(s[i])
            ans=max(ans,i-l+1)
        return ans