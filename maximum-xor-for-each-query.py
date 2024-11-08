class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prevXOR = 0
        k = 2 ** maximumBit - 1
        ans = []
        for i in range(n):
            prevXOR ^= nums[i]
            ans.append(prevXOR ^ k)
        ans = ans[::-1]
        return ans
