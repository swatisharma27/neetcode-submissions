class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x] 

        def union(a, b):
            root_a = find(a) 
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_b] = root_a
            return True

        for n1, n2 in edges:
            union(n1, n2)

        result = set()    
        for i in range(n):
            result.add(find(i))

        return len(result)

