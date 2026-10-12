# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """


# from collections import deque
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = [] if neighbors is None else neighbors


# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         """
#         TC: O(V+E)
#         SC: O(V+E)
#         """

#         ## Edge case
#         if node is None:
#             return None

#         q = deque()
#         q.append(node)

#         freq = {}
#         freq[node] = Node(val=node.val)

#         while q:
#             curr = q.popleft()
#             clone_curr = freq[curr]

#             # neighbors
#             for neigh in curr.neighbors:
#                 if neigh not in freq:
#                     freq[neigh] = Node(val=neigh.val)
#                     q.append(neigh)
#                 clone_curr.neighbors.append(freq[neigh])

#         return freq[node]



from collections import deque
class Node:
    def __init__(self, val=0, neighbors= None):
        self.val = val
        self.neighbors = [] if not neighbors else neighbors


class Solution:
    def cloneGraph(self, node):

        if not node:
            return None

        q = deque()
        q.append(node)

        duplicate = Node(val=node.val)
        freq = {}
        freq[node] = duplicate

        while q:
            curr = q.popleft()
            copy_curr = freq[curr]

            # neighbors
            for i in curr.neighbors:
                if i not in freq:
                    duplicate = Node(i.val)
                    freq[i] = duplicate
                    q.append(i)
                copy_curr.neighbors.append(freq[i])

        return freq[node]

        