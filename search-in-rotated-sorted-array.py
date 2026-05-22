class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_idx(l, r):
            while r - l + 1 > 1:
                mid = l + (r - l) // 2

                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            
            return l


        n = len(nums)
        l, r = 0, n - 1

        if n == 1:
            return 0 if nums[0] == target else -1

        
        min_idx = find_min_idx(l, r)

        if target >= nums[min_idx] and target <= nums[-1]:
            l, r = min_idx, n - 1
        else:
            l, r = 0, min_idx
            
        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1
                    
