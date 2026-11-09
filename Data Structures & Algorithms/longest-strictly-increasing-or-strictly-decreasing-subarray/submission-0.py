class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        curlen=ans=1
        for i in range(1,n):
            if (nums[i]==nums[i-1] or ((nums[i-curlen]<nums[i-curlen+1])!=(nums[i-1]<nums[i]))):
                curlen=1 if (nums[i]==nums[i-1]) else 2
                continue
            curlen+=1
            ans=max(ans,curlen)
        return ans