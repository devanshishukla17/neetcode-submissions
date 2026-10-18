class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stsum=sum(stones)
        tgt=stsum//2
        dp=[0]*(tgt+1)
        for s in stones:
            for t in range(tgt,s-1,-1):
                dp[t]=max(dp[t],dp[t-s]+s)
        return stsum-2*dp[tgt]