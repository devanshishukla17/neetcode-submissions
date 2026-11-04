class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        dist=[-1]*(n*n+1)
        dist[1]=0
        q=[1]
        for cur in q:
            if cur==n*n:
                return dist[cur]
            for landing in range(cur+1,min(cur+6,n*n)+1):
                layer,col=divmod(landing-1,n)
                row=n-1-layer
                if layer%2:
                    col=n-1-col
                target=landing if board[row][col]==-1 else board[row][col]
                if dist[target]==-1:
                    dist[target]=dist[cur]+1
                    q.append(target)
        return -1
