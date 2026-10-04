class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        if len(pattern) != len(word):
            return False
        char={}
        store=set()
        for i,(c,w) in enumerate(zip(pattern,word)):
            if c in char:
                if word[char[c]]!=w:
                    return False
            else:
                if w in store:
                    return False
                char[c]=i
                store.add(w)
        return True