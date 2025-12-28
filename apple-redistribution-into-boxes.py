class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apples = sum(apple)
        used = 0
        
        for i in range(len(capacity)):
            used += capacity[i]
            if used >= total_apples:
                return i + 1

        return -1