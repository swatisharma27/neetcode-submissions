class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        """
        TC: O(m*n)
        SC: O(m*n)
        """

        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                
        if fresh == 0:
            return 0

        minutes = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()

                # neigbours
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    # bounds and original grid to update
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1

        if fresh > 0:
            return -1 

        return minutes

        