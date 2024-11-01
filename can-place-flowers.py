class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i - 1 >= 0:
                    flowerbed[i-1] = 2
                if i + 1 < len(flowerbed):
                    flowerbed[i+1] = 2
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                count += 1
                flowerbed[i] = 1
                if i - 1 >= 0:
                    flowerbed[i-1] = 2
                if i + 1 < len(flowerbed):
                    flowerbed[i+1] = 2
        print(count)
        return True if (flowerbed.count(0) + count) >= n else False
