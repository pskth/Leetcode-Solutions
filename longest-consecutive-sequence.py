class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            1st solution hashset solution
            2nd solution union find implemented via hashmap

            should check why not mp[num] works but
            num not in mp doesnt work
        """
        # nums_set = set(nums)
        # res = 0

        # for num in nums:
        #     if num - 1 not in nums_set:
        #         cur = 1
        #         while num + 1 in nums_set:
        #             cur += 1
        #             num += 1
        #         res = max(res, cur)
        
        # return res

        mp = defaultdict(int)
        res = 0
        """
        num not in mp is True
        but if statement does not execute
        """
        for num in nums:
            print(num not in mp)
            print(not mp[num])
            print(num, mp[num])
            print()
            if num not in mp:
                print(mp[num])
                mp[num] = mp[num + 1] + mp[num - 1] + 1
                print(mp[num])
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])

            # if num == 4:
            #     print(mp)
    
        return res


                
