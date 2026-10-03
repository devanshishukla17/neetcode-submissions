class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans,q=[],[]
        def ksum(k,start,target):
            if k==2:
                l,r=start,n-1
                while l<r:
                    if nums[l]+nums[r]<target:
                        l+=1
                    elif nums[l]+nums[r]>target:
                        r-=1
                    else:
                        ans.append(q+[nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                return
            for i in range(start,n-k+1):
                if i>start and nums[i]==nums[i-1]:
                    continue
                q.append(nums[i])
                ksum(k-1,i+1,target-nums[i])
                q.pop()
        ksum(4,0,target)
        return ans
