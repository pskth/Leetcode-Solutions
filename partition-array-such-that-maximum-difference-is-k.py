class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        numOfSubsequnces = 1

        l = 0
        for r in range(len(nums)):
            if nums[r] - nums[l] > k:
                l = r
                numOfSubsequnces += 1
        
        return numOfSubsequnces

        """
        Tried a different approach but didn't work
        queue = [(1,num) for num in nums]
        ans, curR = 1, 1
        curSmall = curLarge = nums[0]

        while queue:
            r, ele = queue.pop(0)
            print(f"{r=}, {ele=}")
            if r != curR:
                curR += 1
                curLarge = curSmall = ele 
            if abs(curLarge - ele) > k or abs(curSmall - ele) > k:
                ans += 1
                queue.append((r+1,ele))
                continue
            elif ele < curSmall:
                curSmall = ele
            elif ele > curLarge:
                curLarge = ele

        
        return curR
        """