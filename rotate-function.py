class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        prev = 0
        n = len(nums)
        sum_all = 0
        
        for i, num in enumerate(nums):
            prev += i * num
            sum_all += num
        
        res = prev

        for i in reversed(range(len(nums))):
            prev = prev + sum_all - (n * nums[i]) 
            res = max(res, prev)

        return res
