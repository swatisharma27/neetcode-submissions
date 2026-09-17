from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        TC: O(m*n)
        SC: O(m*n)
        """

        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        fresh = 0
        minutes = 0

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while q and fresh > 0:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                # neighbors
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc 
                    # bound check & original
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1
        
        if fresh > 0:
            return -1

        return minutes
                        




                