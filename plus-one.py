class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1

        i = len(digits) - 1
        while i > 0 and digits[i] ==  10:
            digits[i - 1] += 1
            digits[i] = 0
            i -= 1
        
        return [1,0] + digits[1:] if digits[0] == 10 else digits