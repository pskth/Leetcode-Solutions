class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        if len(merged) % 2:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
