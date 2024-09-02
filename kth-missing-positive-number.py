class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # missing = []
        # for i in range(arr[-1]):
        #     if i+1 not in arr:
        #         missing.append(i+1)
        # if k > len(missing):
        #     return arr[-1] + k - len(missing)
        # else:
        #     return missing[k-1]

        #Alternate Solution O(log n)
        
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k
