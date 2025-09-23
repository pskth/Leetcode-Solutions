class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        memo = {}
        ans = []
        cur = []

        def bt(i):
            nonlocal ans, cur
            if i > len(nums) - 1:
                ans.append(cur[:])
                return 

            cur.append(nums[i])
            bt(i + 1)
            cur.pop()

            bt(i + 1)

        bt(0)
        return ans

