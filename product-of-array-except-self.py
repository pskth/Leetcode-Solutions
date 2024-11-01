class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        ans = []

        for i in range(n):
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[-(i + 1)] = postfix[-(i + 1) + 1] * nums[-(1 + i)]

        ans.append(postfix[1])

        for i in range(1, n - 1):
            ans.append(prefix[i - 1] * postfix[i + 1])

        ans.append(prefix[n - 2])

        return ans
