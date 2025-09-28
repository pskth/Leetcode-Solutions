class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def possible(s1, s2, s3):
            if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
                return True
            else:
                return False

        heap = []

        for num in nums:
            heapq.heappush(heap, - num)

        s1 = - heapq.heappop(heap)
        s2 = - heapq.heappop(heap)
        s3 = - heapq.heappop(heap)
        if possible(s1, s2, s3):
            return s1 + s2 + s3

        while heap:
            s1 = s2
            s2 = s3
            s3 = - heappop(heap)

            if possible(s1, s2, s3):
                return s1 + s2 + s3

        return 0