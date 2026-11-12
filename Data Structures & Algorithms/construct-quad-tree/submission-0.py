"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.dfs(grid, len(grid), 0, 0)


    def dfs(self, grid, n, r, c):

        # base
        allSame = True
        for i in range(n):
            for j in range(n):
                if grid[r][c] != grid[r + i][c + j]:
                    allSame = False

        if allSame:
            return Node(grid[r][c], True)

        # logic
        n = n//2
        topLeft = self.dfs(grid, n, r, c)
        topRight = self.dfs(grid, n, r, c+n)
        bottomLeft = self.dfs(grid, n, r+n, c)
        bottomRight = self.dfs(grid, n, r+n, c+n)

        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)


        