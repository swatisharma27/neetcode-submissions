import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key=lambda x:x[0])

        available = list(range(n))
        heapq.heapify(available)

        occupied = [] # endTime, room

        count = [0] * n

        for start, end in meetings:
            duration = end - start

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
                newEnd = endTime + duration
                heapq.heappush(occupied, (newEnd, room))
                count[room] += 1

        max_meetings = max(count)
        roomNum = count.index(max_meetings)
        return roomNum

                







        



        


















































        # # sort the meetings by start time 
        # ## - we need to find smallest available room
        # ## - we need to keep checking for the room that finishes first


        # meetings.sort(key=lambda x:x[0])

        # # create heaps
        # available = list(range(n))
        # heapq.heapify(available) # [0, 1, 2]

        # # occupied heap
        # occupied = [] # (endTime, available room number)

        # # maintain meeting rooms
        # count = [0] * n

        # for start, end in meetings:

        #     duration = end - start

        #     while occupied and start >= occupied[0][0]:
        #         endTime, room = heapq.heappop(occupied)
        #         heapq.heappush(available, room)


        #     if available:
        #         room = heapq.heappop(available) 
        #         newEnd = end
        #         heapq.heappush(occupied, (newEnd, room))
        #         count[room] += 1
        #     else:
        #         endTime, room = heapq.heappop(occupied)
        #         newEnd = endTime + duration
        #         heapq.heappush(occupied, (newEnd, room))
        #         count[room] += 1

        # out = max(count)
        # roomNum = count.index(out) + 1
        # return roomNum





