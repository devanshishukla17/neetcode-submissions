class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap=[]

        for i in intervals:
            if min_heap and min_heap[0]<=i.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,i.end)
        return len(min_heap)