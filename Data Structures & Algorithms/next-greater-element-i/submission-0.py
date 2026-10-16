class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n=len(nums1),len(nums2)
        idx={num:i for i,num in enumerate(nums1)}
        ans=[-1]*m
        st=[]
        for i in range(n):
            cur=nums2[i]
            while st and cur>st[-1]:
                val=st.pop()
                index=idx[val]
                ans[index]=cur
            if cur in idx:
                st.append(cur)
        return ans