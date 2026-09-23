class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avail=[]
        count=[0]*n
        for i in range(n):
            heapq.heappush(avail,(0,i))
        for start,end in meetings:
            while avail and avail[0][0]<start:
                endtime,room=heapq.heappop(avail)
                heapq.heappush(avail,(start,room))
            endtime,room=heapq.heappop(avail)
            heapq.heappush(avail,(endtime+(end-start),room))
            count[room]+=1
        return count.index(max(count))