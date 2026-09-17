from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        result = []

        indegrees = [0] * numCourses
        print(indegrees)
        graph = {}
        for course, preReq in prerequisites:
            graph.setdefault(preReq, []).append(course)
            indegrees[course] += 1

        q = deque()
        N = len(indegrees)
        for course in range(N):
            if indegrees[course] == 0:
                q.append(course)

        count = 0
        while q:
            curr = q.popleft()
            count += 1
            result.append(curr)

            children = graph.get(curr, [])
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)


        if count == numCourses:
            return result
        return []
        