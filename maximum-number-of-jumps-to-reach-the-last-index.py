class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == -1:
                continue

            cur = nums[i]

            for j in range(i+1, n):
                next = nums[j]
                if abs(cur - next) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[-1]
