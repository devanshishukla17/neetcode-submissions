class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ans=[]
        candidates.sort()
        def dfs(idx,path,cur):
            if cur==target:
                ans.append(path.copy())
                return
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if cur+candidates[i]>target:
                    break
                
                path.append(candidates[i])
                dfs(i+1,path,cur+candidates[i])
                path.pop()
        dfs(0,[],0)
        return ans
