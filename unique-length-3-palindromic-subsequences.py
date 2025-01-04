class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
            -if first and last letter is same then its a palindrome (since len is 3)
            -if multiple appearances of a letter, choose the first and last appearance
            ...
            Get the indices of all the characters: first loop
            number of palindromes is the len(set(all the characters betweeen first and last index of a           character))

        '''
        indices = defaultdict(list)
        ans = 0

        for i in range(len(s)):
            indices[s[i]].append(i)

        for index in indices.values():
            if index[-1] - index[0] >= 2:
                ans += len(set(s[index[0]+1:index[-1]]))

        return ans
