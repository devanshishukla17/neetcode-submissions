class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def dfs(i):
            if i==n:
                ans.append(nums.copy())
                return
            for j in range(i,n):
                if j>i and nums[i]==nums[j]:
                    continue
                nums[i],nums[j]=nums[j],nums[i]
                dfs(i+1)
            for j in range(n-1,i,-1):
                nums[j],nums[i]=nums[i],nums[j]
        nums.sort()
        dfs(0)
        return ans