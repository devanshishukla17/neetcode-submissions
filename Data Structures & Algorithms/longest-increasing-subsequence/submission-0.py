import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub=[]
        for num in nums:
            if len(sub)==0 or sub[-1]<num:
                sub.append(num)
            else:
                index=bisect.bisect_left(sub,num)
                sub[index]=num
        return len(sub)