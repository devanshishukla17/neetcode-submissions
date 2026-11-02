class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def c(l,h):
            if l>h:
                return None
            mid=(l+h)//2
            return TreeNode(nums[mid],c(l,mid-1),c(mid+1,h))
        return c(0,len(nums)-1)