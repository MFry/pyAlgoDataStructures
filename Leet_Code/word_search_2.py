class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = dict()
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['*'] = '*'
        self.result = set()
        self.used = [[False for j in range(len(board[i]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.find(i, j, board, '', trie)
        return list(self.result)

    def find(self, i, j, board, prefix, trie):
        if '*' in trie:
            self.result.add(prefix)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return
        c = board[i][j]
        if not self.used[i][j] and c in trie:
            self.used[i][j] = True
            # top
            self.find(i - 1, j, board, prefix + board[i][j], trie[c])
            # left
            self.find(i, j - 1, board, prefix + board[i][j], trie[c])
            # bottom
            self.find(i + 1, j, board, prefix + board[i][j], trie[c])
            # right
            self.find(i, j + 1, board, prefix + board[i][j], trie[c])
            self.used[i][j] = False


if __name__ == '__main__':
    s = Solution()
    print( s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                ["oath", "pea", "eat", "rain"]))
