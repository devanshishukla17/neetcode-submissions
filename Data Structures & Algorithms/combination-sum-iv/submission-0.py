class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp=defaultdict(int)
        dp[target]=1
        for t in range(target,0,-1):
            for num in nums:
                if t<num:
                    break
                dp[t-num]+=dp[t]
        return dp[0]