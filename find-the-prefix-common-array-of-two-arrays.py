class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        n = len(A)
        res = [0] * n
        
        for i in range(n):
            prev_len = len(seen)
            seen.add(A[i])
            seen.add(B[i])
            cur_len = len(seen)
            
            res[i] = res[i - 1] + (2 - (cur_len - prev_len))

        return res


"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_A = set()
        seen_B = set()
        n = len(A)
        C = [0] * n

        for i in range(n):
            if A[i] in seen_B:
                C[i] += 1
            seen_A.add(A[i])

            if B[i] in seen_A:
                C[i] += 1
            seen_B.add(B[i])

        prev = C[0]
        for i in range(1,n):
            C[i] += prev
            prev = C[i]

        return C
"""
