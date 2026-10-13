class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        TC: O(V+E)
        SC: O(V+E)
        """
        
        # no nodes, empty graph = True
        if not n:
            return True

        # adjacency
        graph = {}
        for n1, n2 in edges:
            graph.setdefault(n1, []).append(n2)
            graph.setdefault(n2, []).append(n1)

        visited = set()

        return self.dfs(0, -1, visited, graph) and n == len(visited)

    def dfs(self, curr, prev, visited, graph):

        # base
        if curr in visited:
            return False

        # action
        visited.add(curr)

        # logic
        neighbors = graph.get(curr, [])
        for neigh in neighbors:
            if neigh == prev:
                continue
            call = self.dfs(neigh, curr, visited, graph)
            if not call:
                return False

        return True

            


