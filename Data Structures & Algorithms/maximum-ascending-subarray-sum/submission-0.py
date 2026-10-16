class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=cursum=nums[0]
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                cursum=0
            cursum+=nums[i]
            ans=max(ans,cursum)
        return ans