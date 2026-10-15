class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord==endWord):
            return 0
        w,ans=set(wordList),0
        q=deque([beginWord])
        while q:
            ans+=1
            for _ in range(len(q)):
                node=q.popleft()
                if node==endWord:
                    return ans
                for i in range(len(node)):
                    for c in range(97,123):
                        if chr(c)==node[i]:
                            continue
                        nei=node[:i]+chr(c)+node[i+1:]
                        if nei in w:
                            q.append(nei)
                            w.remove(nei)
        return 0