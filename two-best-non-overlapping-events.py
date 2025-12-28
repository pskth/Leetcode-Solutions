class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        max_val = [events[-1][2]]
        for i in range(len(events)-2, -1, -1):
            max_val.append(max(max_val[-1], events[i][2]))
        max_val.reverse()
        
        ans = events[0][2]
        for event in events:
            idx = bisect.bisect_right(events, event[1], key = lambda x:x[0])
            ans = max(ans, event[2])
            if idx != len(events):
                ans = max(ans, event[2]+max_val[idx])
        return ans