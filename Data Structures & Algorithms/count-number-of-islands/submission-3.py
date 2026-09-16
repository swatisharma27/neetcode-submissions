# class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:

    #     rows = len(grid)
    #     cols = len(grid[0])
    #     dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     count = 0
        
    #     for i in range(rows):
    #         for j in range(cols):  
              
    #             if grid[i][j] == "1":
    #                 count += 1
    #                 q = deque()
    #                 q.append((i, j))
    #                 grid[i][j] = "0"

    #                 while q:
    #                     r, c = q.popleft()
                        
    #                     for dr, dc in dirs:
    #                         nr = r + dr
    #                         nc = c + dc

    #                         if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1":
    #                             q.append((nr, nc))
    #                             grid[nr][nc] = "0"
    #     return count

class Solution:
    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j, rows, cols)
        return count


    def dfs(self, grid, i , j, rows, cols):

        # base
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
            return 

        # action
        grid[i][j] = "0"

        # logic
        dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in dirs:
            nr = dr + i
            nc = dc + j

            self.dfs(grid, nr, nc, rows, cols)




    
        

    