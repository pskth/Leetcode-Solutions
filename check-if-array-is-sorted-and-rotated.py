class Solution:
    def check(self, nums: List[int]) -> bool:
        dec = 0
        n = len(nums)
         
        for i in range(1,n):
            if nums[i] < nums[i - 1]:
                dec += 1
            if dec == 1:
                break
        
        if dec == 0:
            return True
        
        a = list(list(reversed(nums[:i])) + list(reversed(nums[i:])))

        for i in range(1,n):
            if a[i] > a[i - 1]:
                return False

        return True
