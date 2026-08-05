class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(largest):
            sub=1
            current=0
            for num in nums:
                current+=num
                if current>largest:
                    sub+=1
                    if sub>k:
                        return False
                    current=num
            return True
        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            mid=l+(r-l)//2
            if split(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res