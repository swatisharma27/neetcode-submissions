class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for el in nums:
            freq[el] = freq.get(el, 0) + 1

        N = len(nums)
        buckets = [[] for _ in range(N+1)]

        for el, count in freq.items():
            buckets[count].append(el)

        result = []
        for i in range(N, 0, -1):
            for el in buckets[i]:
                result.append(el)
                if len(result) == k:
                    return result
