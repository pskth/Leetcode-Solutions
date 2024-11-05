class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapify(arr)
        count = 0
        while (count < k - 1):
            count += 1
            heappop(arr)
        return -heappop(arr)
