class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            l1, l2 = self.checkPalindrome(i, i, s)
            l3, l4 = self.checkPalindrome(i, i+1, s)

            if l2-l1 > end-start:
                start, end = l1, l2
            if l4-l3 > end-start:
                start, end = l3,l4
        
        return s[start:end+1]
        

    def checkPalindrome(self, i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return i + 1, j - 1