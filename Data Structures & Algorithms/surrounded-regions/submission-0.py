class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        def capt(r,c):
            if (r<0 or c<0 or r==rows or c==cols or board[r][c]!="O"):
                return
            board[r][c]="T"
            capt(r+1,c)
            capt(r-1,c)
            capt(r,c+1)
            capt(r,c-1)
        for r in range(rows):
            if board[r][0]=="O":
                capt(r,0)
            if board[r][cols-1]=="O":
                capt(r,cols-1)
        for c in range(cols):
            if board[0][c]=="O":
                capt(0,c)
            if board[rows-1][c]=="O":
                capt(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"