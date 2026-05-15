class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        observations:
        sorted array is rotated
        all unique elements
        O(logn) -> maybe binary search
        
        Used book and pen,
        observed that we can pick mid ele, if last ele of array
        larger then min is not in 2nd half else it is.
        works becz sorted.
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        l, r, = 0, n - 1
        while r - l + 1 > 1:
            mid = l + (r - l) // 2
            if nums[mid] < nums[(mid + 1) % n] and nums[mid] < nums[mid - 1]:
                return nums[mid] 
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1            
        return nums[l]
