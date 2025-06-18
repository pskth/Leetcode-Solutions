class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i % 3 == 2:
                ans.append(nums[i - 2 : i + 1])
                continue
            if i % 3 == 0 and  nums[i + 2] - nums[i] > k:
                return []

        return ans
