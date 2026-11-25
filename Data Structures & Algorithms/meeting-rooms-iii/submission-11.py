class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        import heapq

        available = list(range(n))
        heapq.heapify(available) # 0,1,2

        occupied = [] #(end, roomNum)

        count = [0] * n

        meetings.sort(key=lambda x: x[0])

        for start, end in meetings:
            duration = end - start

            while occupied and occupied[0][0] <= start:
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(available, room)


            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
                count[room] += 1

            else:
                newEnd, room = heapq.heappop(occupied)
                delay = newEnd + duration
                heapq.heappush(occupied, (delay, room))
                count[room] += 1


        max_rooms = max(count)
        roomNum = count.index(max_rooms)
        return roomNum








