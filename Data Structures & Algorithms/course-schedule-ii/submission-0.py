class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq={c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        ans=[]
        vis,cyc=set(),set()
        def dfs(crs):
            if crs in cyc:
                return False
            if crs in vis:
                return True
            cyc.add(crs)
            for pre in prereq[crs]:
                if dfs(pre)==False:
                    return False
            cyc.remove(crs)
            vis.add(crs)
            ans.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return ans