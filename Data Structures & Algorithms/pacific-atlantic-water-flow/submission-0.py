class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        pq = deque()
        aq = deque()

        p_set = set()
        a_set = set()

        ## ADD TO QUEUE - PACIFIC & ATLANTIC; ALSO respective SETS
        # left col
        for r in range(rows):
            pq.append((r, 0))
            p_set.add((r, 0))

        # top row
        for c in range(cols):
            pq.append((0, c))
            p_set.add((0, c))

        # right col
        for r in range(rows):
            aq.append((r, cols-1))
            a_set.add((r, cols-1))        

        # bottom row
        for c in range(cols):
            aq.append((rows-1, c))
            a_set.add((rows-1, c))

        
        ## NEIGHBORS CHECK + BOUND CHECK
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            r, c = pq.popleft()

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c]:
                    if (nr, nc) not in p_set:
                        pq.append((nr, nc))
                        p_set.add((nr, nc))

        while aq:
            r, c = aq.popleft()

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c]:
                    if (nr, nc) not in a_set:
                        aq.append((nr, nc))
                        a_set.add((nr, nc))

        
        result = []
        for i in p_set:
            if i in a_set:
                result.append(i)

        return result











