class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans,cur=[],[]
        used=[False]*n
        def back():
            if len(cur)==n:
                ans.append(cur.copy())
                return
            for i in range(n):
                if used[i]==False:
                    cur.append(nums[i])
                    used[i]=True
                    back()
                    cur.pop()
                    used[i]=False
        back()
        return ans