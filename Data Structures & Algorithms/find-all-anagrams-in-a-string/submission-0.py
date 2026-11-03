class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need,win=[0]*26,[0]*26
        for c in p:
            need[ord(c)-97]+=1
        ans=[]
        for i,c in enumerate(s):
            win[ord(c)-97]+=1
            if i>=len(p):
                win[ord(s[i-len(p)])-97]-=1
            if i+1>=len(p) and win==need:
                ans.append(i+1-len(p))
        return ans