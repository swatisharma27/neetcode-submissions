class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                # Rows
                for j in range(9):
                    if j != c and val == board[r][j]:
                        return False

                # Columns
                for i in range(9):
                    if i != r and val == board[i][c]:
                        return False

                ## Squares
                start_r = r//3 * 3
                start_c = c//3 * 3

                for m in range(start_r, start_r + 3):
                    for n in range(start_c, start_c + 3):
                        if (m,n) != (r,c) and val == board[m][n]:
                            return False


        return True