class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oddHeap = []
        evenHeap = []
        for i in range(len(nums)):
            if nums[i] & 1:
                heapq.heappush(oddHeap, i)
            else:
                heapq.heappush(evenHeap, i)

        oddCount = len(oddHeap)
        evenCount = len(evenHeap)
        ans = 0
        if abs(oddCount - evenCount) > 1:
            return -1
        elif len(nums)&1:
            parity = 1 if oddCount > evenCount else 0
            for i in range(0, len(nums), 2):
                if parity:
                    ans += abs(i - heapq.heappop(oddHeap))
                else:
                    ans += abs(i - heapq.heappop(evenHeap))
        else:
            parity = 1
            oddAns = evenAns = 0
            for i in range(0, len(nums), 2):
                oddAns += abs(i - heapq.heappop(oddHeap))

            parity = 0
            for i in range(0, len(nums), 2):
                evenAns += abs(i - heapq.heappop(evenHeap))

            ans = min(oddAns, evenAns)
        
        return ans