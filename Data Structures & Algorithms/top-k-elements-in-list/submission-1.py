class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        freq = Counter(nums)
        return [i[0] for i in list(freq.most_common(k))]

        
