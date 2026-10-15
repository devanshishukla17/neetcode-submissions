class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        visit = [0] * n

        def diff(s1, s2):
            cur = 0
            for i in range(min(len(s1),len(s2))):
                if s1[i] != s2[i]:
                    cur += 1
            return cur
        table = {}
        q = collections.deque()
        q.append(beginWord)
        q.append("")
        ans = 1
        while q:
            cur = q.popleft()
            if cur == "":
                if q:
                    ans += 1
                    q.append("")
                continue
            for i in range(n):
                if visit[i] == 1:
                    continue
                word = wordList[i]
                if diff(cur, word) == 1:
                    if word == endWord:
                        return ans + 1
                    visit[i] = 1
                    q.append(word)
        return 0

