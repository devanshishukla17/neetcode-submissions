class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        def dfs(i,cur,total):
            if total==target:
                ans.append(cur.copy())
                return 
            for j in range(i,n):
                if total+nums[j]>target:
                    return
                cur.append(nums[j])
                dfs(j,cur,total+nums[j])
                cur.pop()
        dfs(0,[],0)
        return ans