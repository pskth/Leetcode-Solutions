class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append((i, temp))
        
        return res
