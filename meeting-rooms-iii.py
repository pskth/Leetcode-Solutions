class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_time_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability_time[i] <= start:
…
        return meeting_count.index(max(meeting_count))