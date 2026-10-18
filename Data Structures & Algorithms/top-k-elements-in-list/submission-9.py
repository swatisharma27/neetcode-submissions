class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        result = []
        N = len(nums)
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        buckets = [[] for i in range(N+1)]
        
        for num, count in freq.items():
            buckets[count].append(num)

        for i in range(N, -1, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result








        