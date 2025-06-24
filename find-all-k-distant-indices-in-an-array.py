class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        k_distant_indices = []
        queue = [j for j in range(n) if nums[j] == key]

        i = 0
        flag = 0
        while i < n and queue:
            if abs(i - queue[0]) <= k:
                k_distant_indices.append(i)
                flag = 1
            elif flag:
                flag = 0
                queue.pop(0)
                i -= 1
            i += 1

        return k_distant_indices
