class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        def back(i,sub):
            ans.append(sub[::])
            for j in range(i,n):
                if j>i and nums[j]==nums[j-1]:
                    continue
                sub.append(nums[j])
                back(j+1,sub)
                sub.pop()
        back(0,[])
        return ans