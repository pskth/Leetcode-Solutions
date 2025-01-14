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
