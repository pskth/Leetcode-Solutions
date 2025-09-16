class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' Not Efficient code, just tried a solution'''
        curSum = 0
        cur_arr = []
        ans = []
        seen = set()

        def bt(i,curSum):
            nonlocal cur_arr, ans
            if curSum == target:
                ##print("in if: ", cur_arr, ans)
                if tuple(cur_arr) not in seen:
                    seen.add(tuple(cur_arr))
                    ans.append(cur_arr[:])
                return
            if i == len(candidates) or curSum > target:
                return

            curSum += candidates[i]
            cur_arr += [candidates[i]]
            bt(i, curSum)
            curSum -= candidates[i]
            cur_arr.pop()

            curSum += candidates[i]
            cur_arr += [candidates[i]]
            #print(cur_arr)
            bt(i + 1, curSum)
            curSum -= candidates[i]
            cur_arr.pop()

            bt(i + 1, curSum)

        bt(0, curSum)
        return ans