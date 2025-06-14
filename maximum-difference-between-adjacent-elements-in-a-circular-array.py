class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        l = -1
        r = 0
        maxAbsDiff = 0

        while r < len(nums):
            maxAbsDiff = max(maxAbsDiff, abs(nums[l] - nums[r]))
            l += 1
            r += 1

        return maxAbsDiff