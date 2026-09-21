from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        TC: O(m*n)
        SC: O(m*n)
        """
        
        rows = len(board)
        cols = len(board[0])

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                    if board[i][j] == 'O':
                        board[i][j] = 'S'
                        q.append((i,j))

        while q:
            r,c = q.popleft()
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c

                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    q.append((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                                        
  


                        
