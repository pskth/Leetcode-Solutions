class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes * 6
        h = hour + minutes / 60
        hour_angle = h * 360 / 12

        return min(abs(min_angle - hour_angle), 360 - abs(min_angle - hour_angle))
