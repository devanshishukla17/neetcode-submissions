class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l=len(tasks)
        cnt=[0]*26
        for t in tasks:
            cnt[ord(t)-ord('A')]+=1
        maxf=max(cnt)
        maxc=0
        for i in cnt:
            maxc+=1 if i==maxf else 0
        time=(maxf-1)*(n+1)+maxc
        return max(l,time)
