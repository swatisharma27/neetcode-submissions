class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        N = len(nums)
        freq = {}
        resultArr = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(N+1)]

        for num, count in freq.items():
            bucket[count].append(num)

        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                resultArr.append(j)
                if len(resultArr) == k:
                    return resultArr
