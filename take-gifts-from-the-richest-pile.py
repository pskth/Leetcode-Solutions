class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        
        while k > 0:
            k -= 1
            maxGifts = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(maxGifts)))
        
        return -sum(gifts)
