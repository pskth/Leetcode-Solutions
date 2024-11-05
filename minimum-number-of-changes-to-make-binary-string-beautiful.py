class Solution:
    def minChanges(self, s: str) -> int:
        """
        Idea was to choose either 1 or 0 (there was some reasoning or intution)
        Then keep track of count.
        if 0's ended in odd no. make the last zero as 1
        if 1's ended in odd no. make the 0 next to last 1 as 1
        This method will prolly make the sets of largest size possible
        """
        '''
        Optimal Soln:
        Since size of string is even and every set needs to be even lengthed.
        Starting from 0th index, check each pair by incrementing loop by 2
        if each element in pair don't match then ans++
        '''
        count = 0
        prev = s[0]
        ans = 0
        for i in range(len(s)):
            if s[i] == prev:
                count += 1
                prev = s[i]
            elif count % 2 == 0:
                count = 1
                prev = s[i]
            elif prev == 1:
                ans += 1
                count = 0
                prev = '1'
            else:
                count = 2
                ans += 1
                prev = '1'
        return ans
