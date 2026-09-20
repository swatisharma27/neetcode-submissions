class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        dist = 1
        while q:
            size = len(q)

            for _ in range(size):
                r, c = q.popleft()

                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]== 2147483647:
                        grid[nr][nc]= dist
                        q.append((nr, nc))
            dist += 1
