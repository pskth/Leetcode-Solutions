class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        remBottles = drank = numBottles

        while remBottles >= numExchange:
            newBottles = 1
            drank += newBottles
            remBottles = newBottles + (remBottles - numExchange)
            numExchange += 1

        return drank