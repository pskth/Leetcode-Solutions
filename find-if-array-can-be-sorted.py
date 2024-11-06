'''
Intution was that since we are need to swap each adjacent element and sort we can use bubble sort and make a swap only if number of 1's are same in both swapiees. Finally check if the resultant array is same as originalarray.sort()
worked becz len(arr) MAX is 100.
'''
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        seen = {}
        def countOnes(a: int,b: int) -> bool:
            countA, countB = 0, 0
            
            if a in seen:
                countA = seen[a]
            else:
                binA = bin(a)[2:]
                for i in binA:
                    if i == '1':
                        countA += 1
                seen[a] = countA
            
            if b in seen:
                countB = seen[b]
            else:
                binB = bin(b)[2:]
                for j in binB:
                    if j == '1':
                        countB += 1
                seen[b] = countB

            return countA == countB

        temp = nums.copy()
        temp.sort()
        n = len(nums)
        for i in range(n):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    if countOnes(nums[j],nums[j+1]):
                        nums[j],nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False
        return nums == temp
