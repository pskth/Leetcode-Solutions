class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remBottles = drank = numBottles

        while remBottles >= numExchange:
            print(remBottles)
            newBottles = remBottles // numExchange
            drank += newBottles
            remBottles = newBottles + (remBottles % numExchange)

        return drank