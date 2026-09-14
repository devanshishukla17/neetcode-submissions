class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word
        ans = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            ch = board[r][c]
            if ch not in node:
                return
            next_node = node[ch]
            if "#" in next_node:
                ans.append(next_node["#"])
                del next_node["#"]
            board[r][c] = "#"

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            board[r][c] = ch
            if not next_node:
                del node[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return ans