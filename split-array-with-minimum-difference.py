class Solution:
    def splitArray(self, nums: List[int]) -> int:
        flag = 0
        left = right = 0
        peak = 0
        stack = nums[0]
        
        for i in range(1, len(nums)):
            inc = nums[i]
            
            if inc > stack:
                if flag:
                    return -1
                    
                left += stack
                stack = inc

            elif inc < stack:
                if not flag:
                    peak = stack
                flag = 1
                right += inc
                stack = inc

            elif inc == stack:
                if flag:
                    return -1
                flag = 1
                left += stack
                right += inc
                stack = inc


        if not flag:
            return abs(left - inc)
            
        if peak:
            if right - left > 0:
                left += peak
            else:
                right += peak

        return abs(right - left)