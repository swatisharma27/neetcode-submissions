import heapq
from queue import deque
class Solution:

    """
    Ex 1:
    tasks = ["X","X","Y","Y"], n = 2
    {X: 2, Y: 2}
    X Y _ X Y

    Ex 2:
    tasks = ["A","A","A","B","C"], n = 3
    {A: 3, B: 1, C: 1}

    A _ _ _ A _ _ _ A = 9
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = {}
        N = len(tasks)
        for i in range(N):
            freq[tasks[i]] = freq.get(tasks[i], 0) + 1
            

        maxheap = [-i for i in list(freq.values())]
        heapq.heapify(maxheap)
        # -3, -2, -1

        q = deque()
        time = 0

        while maxheap or q:

            time += 1
            
            if maxheap:
                count = heapq.heappop(maxheap)
                count += 1

                if count != 0:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                popped = q.popleft()
                heapq.heappush(maxheap, popped[0])

        return time












        

    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     N = len(tasks)
        
    #     result = 0

    #     freq = {}
    #     N = len(tasks)
    #     for i in range(N):
    #         freq[tasks[i]] = freq.get(tasks[i], 0) + 1

    #     maxFreq = max(freq.values())
    #     maxFreqCount = 0
    #     for i in freq:
    #         if freq[i] == maxFreq:
    #            maxFreqCount += 1 


    #     partitions = maxFreq - 1
    #     availability = partitions * (n - (maxFreqCount-1))
    #     pending = N - (maxFreq * maxFreqCount)
    #     idle = max(0, availability - pending)

    #     result = N + idle

    #     return result
