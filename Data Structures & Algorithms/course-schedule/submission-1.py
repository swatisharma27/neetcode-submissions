# from collections import deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         """
#         TC: O(V+E
#         SC: O(V+E)
#         """
        
#         ## indegrees -> count of the prerequisites for each course
#         ## graph -> [preq: courses]
#         indegrees = [0] * numCourses
#         graph = {}
#         for course, prereq in prerequisites:
#             graph.setdefault(prereq, []).append(course)
#             indegrees[course] += 1

#         ## Process the independent nodes first, add to queue
#         ## nodes with 0
#         q = deque()
#         N = len(indegrees)
#         for course in range(N):
#             if indegrees[course] == 0:
#                 q.append(course)

#         ## Node popped from queue = Processed node => count++
#         count = 0
#         while q:
#             curr = q.popleft()
#             count += 1

#             children = graph.get(curr, [])
#             for child in children:
#                 indegrees[child] -= 1
#                 if indegrees[child] == 0:
#                     q.append(child)
        
#         return count == numCourses


from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ## Create indegrees array of course count
        indegrees = numCourses * [0]
        graph = {}

        ## Traverse prerequisites to store {preq: course} mapping [+] Count the courses and store indegrees
        for course, preq in prerequisites:
            graph.setdefault(preq, []).append(course)
            indegrees[course] += 1 ## tracks preq dependency

        ## Add the nodes in indegrees with 0 dependency
        q = deque()
        N = len(indegrees)
        for course in range(N):
            if indegrees[course] == 0:
                q.append(course)

        ## Node popped and process children
        count = 0
        while q:
            curr = q.popleft()
            count += 1

            children = graph.get(curr, [])
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)

        return count == numCourses


            

        