class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx={c: i for i,c in enumerate(order)}
        def compare(w):
            return [idx[c] for c in w]
        return words==sorted(words,key=compare)