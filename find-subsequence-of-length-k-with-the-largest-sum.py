class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [num[1] for num in sorted(sorted(enumerate(nums), key=lambda pair: pair[1], reverse=True)[:k])]