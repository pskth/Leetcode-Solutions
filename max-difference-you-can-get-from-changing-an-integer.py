class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l, ans = 0, -1
        
        for r in range(1,len(nums)):
            if nums[l] >= nums[r]:
                l = r
                continue
            else:
                ans = max(ans, nums[r] - nums[l])

        return ans 
