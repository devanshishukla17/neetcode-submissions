# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            if not node:
                return 0
            ans=1 if node.val>=maxval else 0
            maxval=max(maxval,node.val)
            ans+=dfs(node.left,maxval)
            ans+=dfs(node.right,maxval)
            return ans
        return dfs(root,root.val)