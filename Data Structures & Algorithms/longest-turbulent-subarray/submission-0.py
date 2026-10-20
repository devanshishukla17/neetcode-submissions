class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        ans=cnt=0
        s=-1
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                cnt=cnt+1 if s==0 else 1
                s=1
            elif arr[i]<arr[i+1]:
                cnt=cnt+1 if s==1 else 1
                s=0
            else:
                cnt=0
                s=-1
            ans=max(ans,cnt)
        return ans+1