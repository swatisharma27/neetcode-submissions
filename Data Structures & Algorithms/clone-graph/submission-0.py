"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        ## Edge case
        if node is None:
            return None

        q = deque()
        q.append(node)

        freq = {}
        freq[node] = Node(val=node.val)

        while q:
            curr = q.popleft()
            clone_curr = freq[curr]

            # neighbors
            for neigh in curr.neighbors:
                if neigh not in freq:
                    freq[neigh] = Node(val=neigh.val)
                    q.append(neigh)
                clone_curr.neighbors.append(freq[neigh])

        return freq[node]

        
        