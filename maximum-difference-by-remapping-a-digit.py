class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxNum = num
        numStr = str(num)
        for i in range(len(numStr)):
            if numStr[i] != "9":
                maxNum = int(numStr.replace(numStr[i], '9'))
                break
        
        minNum = num
        numStr = str(num)
        minNum = int(numStr.replace(numStr[0], '0'))

        return maxNum - minNum