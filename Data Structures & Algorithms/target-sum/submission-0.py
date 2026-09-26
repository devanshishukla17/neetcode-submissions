class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for n in nums:
            dp1=defaultdict(int)
            for total,cnt in dp.items():
                dp1[total+n]+=cnt
                dp1[total-n]+=cnt
            dp=dp1
        return dp[target]