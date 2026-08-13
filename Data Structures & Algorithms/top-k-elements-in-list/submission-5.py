class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # from collections import Counter
        # freq = Counter(nums)
        # return [i[0] for i in list(freq.most_common(k))]

        ################ MIN HEAP + HASHMAP ##############
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        
        # ## most freq elements - min heap() by default in python
        # import heapq

        # pq = [] ## heap defined
        # for num, count in freq.items():
        #     heapq.heappush(pq, (count, num)) ## min heap will not be sorted but pq[0]-top element will be smallest always

        #     if len(pq) > k:
        #         heapq.heappop(pq)

        # return [num[1] for num in pq]
        ##################################################

        ############ Bucket Sort ###############
        """
        TC: O(n)
        SC: O(n)
        """
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 

        buckets = [[] for _ in range(len(nums)+1)]

        # for num, count in freq.items():
        #     buckets[count].append(num)

        # for i in range(len(buckets)-1, 0, -1):
        #     for n in buckets[i]:
        #         result.append(n)
        #         if len(result) == k:
        #             return result   


        for i in range(len(buckets)-1, 0, -1):
            for num, count in freq.items():
                if i == count:
                    buckets[count].append(num)
                    result.append(num)
                    if len(result) == k:
                        return result      

            