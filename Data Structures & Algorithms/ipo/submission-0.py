class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        ind=list(range(n))
        ind.sort(key=lambda x: capital[x])
        maxp,idx=[],0
        for _ in range(k):
            while idx<n and capital[ind[idx]]<=w:
                heapq.heappush(maxp,-profits[ind[idx]])
                idx+=1
            if not maxp:
                break
            w+=-heapq.heappop(maxp)
        return w