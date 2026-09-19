class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l,total=0,0
        ans=float("inf")
        for r in range(n):
            total+=nums[r]
            while total>=target:
                ans=min(r-l+1,ans)
                total-=nums[l]
                l+=1
        return 0 if ans==float("inf") else ans