class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for i in range(rows):
            for j in range(cols):
                dist = 0
                if grid[i][j] == 1:
                    q = deque()
                    q.append((i, j))
                    dist += 1
                    grid[i][j] = -1

                    while q:
                        r, c = q.popleft()

                        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
                        for dr, dc in dirs:
                            nr = dr + r
                            nc = dc + c
                            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                                q.append((nr, nc))
                                grid[nr][nc] = -1
                                dist += 1
                    result = max(result, dist)
        return result