class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col,posdiag,negdiag=set(),set(),set()
        ans=[]
        board=[["."] *n for i in range(n)]
        def back(r):
            if r==n:
                copy=["".join(row) for row in board]
                ans.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"
                back(r+1)
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]="."
        back(0)
        return ans