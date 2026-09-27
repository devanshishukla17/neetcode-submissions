class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=cursum=0
        presum={0:1}
        for num in nums:
            cursum+=num
            diff=cursum-k
            ans+=presum.get(diff,0)
            presum[cursum]=1+presum.get(cursum,0)
        return ans