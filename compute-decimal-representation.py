class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        arr = []
        k = 1
        while n > 0:
            dig = n % 10
            if dig != 0:
                arr.append(k * dig)
            k *= 10
            n //= 10
        return arr[::-1]