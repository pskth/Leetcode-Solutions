class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        while not self.isSorted(nums):
            res += 1
            cur_sum = 0
            min_sum = math.inf
            idx = -1
            for i in range(len(nums) - 1):
…        
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                # print(nums, False)
                return False
        # print(nums, True)
        return True