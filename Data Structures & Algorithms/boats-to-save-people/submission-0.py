class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans,l,r=0,0,len(people)-1
        while l<=r:
            rem=limit-people[r]
            r-=1
            ans+=1
            if l<=r and rem>=people[l]:
                l+=1
        return ans