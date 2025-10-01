class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remBottles = drank = numBottles

        while remBottles >= numExchange:
            newBottles = remBottles // numExchange
            drank += newBottles
            remBottles = newBottles + (remBottles % numExchange)

        return drank