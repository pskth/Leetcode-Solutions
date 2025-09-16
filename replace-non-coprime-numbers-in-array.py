class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)
            while len(stack) > 1 and math.gcd(stack[-1], stack[-2]) > 1:
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(math.lcm(temp1, temp2))    

        return stack