class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binStrings = []
        n = len(nums[0])
        nums = set(nums)
        flag = 0

        def backtrack(curString: str):
            nonlocal flag
            if len(curString) == n:
                if curString not in nums:
                    flag = 1
                binStrings.append(curString)
                return True

            for bit in '01':
                backtrack(curString + bit)
                if flag == 1:
                    return True

            return False
        
        backtrack('')
        return binStrings[-1]
