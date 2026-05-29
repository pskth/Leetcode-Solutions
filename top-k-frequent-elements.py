class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums))]
        d = Counter(nums)

        for i, n in d.items():
            freq[n - 1].append(i)

        res = []

        for i in reversed(range(len(nums))):
            if len(res) >= k:
                break
            if freq[i]:
                res += freq[i]
        
        return res
