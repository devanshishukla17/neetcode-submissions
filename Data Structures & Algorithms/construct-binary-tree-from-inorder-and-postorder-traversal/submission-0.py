# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postidx=inidx=len(postorder)-1
        def dfs(limit):
            nonlocal postidx,inidx
            if postidx<0:
                return None
            if inorder[inidx]==limit:
                inidx-=1
                return None
            root=TreeNode(postorder[postidx])
            postidx-=1
            root.right=dfs(root.val)
            root.left=dfs(limit)
            return root
        return dfs(float('inf'))