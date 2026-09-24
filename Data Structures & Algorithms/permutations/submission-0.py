class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        perm=self.permute(nums[1:])
        ans=[]
        for p in perm:
            for i in range(len(p)+1):
                pcopy=p.copy()
                pcopy.insert(i,nums[0])
                ans.append(pcopy)
        return ans