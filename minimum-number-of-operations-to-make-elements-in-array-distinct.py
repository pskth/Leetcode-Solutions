class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lastRepeat = -1
        visited = dict()

        for i in range(len(nums)):
            if nums[i] in visited:
                lastRepeat = max(lastRepeat, visited[nums[i]])
            visited[nums[i]] = i+1

        return math.ceil(lastRepeat / 3) if lastRepeat != -1 else 0
        
