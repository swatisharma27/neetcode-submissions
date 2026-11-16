import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        TC: O(M logM + M logN)
        SC: O(N)
        """

        meetings.sort(key=lambda x:x[0])

        available = list(range(n))
        heapq.heapify(available) # 0, 1, 2

        occupied = [] # (endTime, room)
        
        count = [0] * n

        for start, end in meetings:

            while occupied and start >= occupied[0][0]:
                endTime, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                newEnd = end
                heapq.heappush(occupied, (newEnd, room))
                count[room] += 1
            else:
                endTime, room = heapq.heappop(occupied)
                duration = end - start
                newEnd = endTime + duration
                heapq.heappush(occupied, (newEnd, room))
                count[room] += 1

        max_room = max(count)
        roomNum = count.index(max_room)
        return roomNum



    