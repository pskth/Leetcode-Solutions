class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curSum = 0
        count = 0

        for i in range(1,n+1):
            if i in banned:
                print(i)
                continue
            if curSum > maxSum:
                return count - 1
            curSum += i
            count += 1
        
        return count if curSum <= maxSum else count - 1
