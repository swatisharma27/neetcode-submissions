import heapq
class MedianFinder:

    def __init__(self):
        self.smallHeap = [] # maxHeap
        self.largeHeap = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)

        # make sure every num in smallHeap is small <= every num in largeHeap
        if self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0]) > self.largeHeap[0]:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -1 * val)

        # make sure elements are almost equal in smallHeap and largeHeap
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -1 * val)
    
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)


    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0]

        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]

        return ((-1 * self.smallHeap[0]) + self.largeHeap[0])/2
