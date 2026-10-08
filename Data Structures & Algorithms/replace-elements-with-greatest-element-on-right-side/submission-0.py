class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n
        rmax=-1
        for i in range(n-1,-1,-1):
            ans[i]=rmax
            rmax=max(arr[i],rmax)
        return ans