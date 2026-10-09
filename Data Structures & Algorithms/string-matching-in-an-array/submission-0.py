from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n=len(words)
        words.sort(key=len)
        ans= []
        for i in range(n):
            for j in range(i + 1,n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break  
        return ans