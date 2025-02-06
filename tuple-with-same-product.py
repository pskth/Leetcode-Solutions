class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        table = {}
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]

                if prod not in table:
                    table[prod] = (nums[i], nums[j])
                    
                elif nums[i] not in table[prod] and nums[j] not in table[prod]:
                    count += 8 * (len(table[prod]) // 2)
                    table[prod] += (nums[i], nums[j])

        return count
