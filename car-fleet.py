class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        stack = []

        for p, s in cars:
            time_to_reach_target = (target - p) / s
            stack.append(time_to_reach_target)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
