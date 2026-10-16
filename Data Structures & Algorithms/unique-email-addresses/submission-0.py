class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uni=set()
        for e in emails:
            loc,dom=e.split('@')
            loc=loc.split('+')[0]
            loc=loc.replace(".","")
            uni.add((loc,dom))
        return len(uni)