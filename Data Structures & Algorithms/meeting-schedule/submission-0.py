class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        n=len(intervals)
        for i in range(1,n):
            a=intervals[i-1]
            b=intervals[i]
            if a.end>b.start:
                return False
        return True
