import unittest


def boggle_lookup_dfs(words, boggle, i, j, prefix, visited_board, words_seen):
    if prefix in words:
        words_seen.add(prefix)
    if i < 0 or j < 0 \
            or i >= len(visited_board) or j >= len(visited_board[i]) \
            or visited_board[i][j]:
        return words_seen
    visited_board[i][j] = True
    c = boggle[i][j]
    # top
    boggle_lookup_dfs(words, boggle, i + 1, j, prefix + c, visited_board, words_seen)
    # top-right
    boggle_lookup_dfs(words, boggle, i + 1, j + 1, prefix + c, visited_board, words_seen)
    # right
    boggle_lookup_dfs(words, boggle, i, j + 1, prefix + c, visited_board, words_seen)
    # bottom-right
    boggle_lookup_dfs(words, boggle, i - 1, j + 1, prefix + c, visited_board, words_seen)
    # bottom
    boggle_lookup_dfs(words, boggle, i - 1, j, prefix + c, visited_board, words_seen)
    # bottom-left
    boggle_lookup_dfs(words, boggle, i - 1, j - 1, prefix + c, visited_board, words_seen)
    # left
    boggle_lookup_dfs(words, boggle, i, j - 1, prefix + c, visited_board, words_seen)
    # top-left
    boggle_lookup_dfs(words, boggle, i + 1, j - 1, prefix + c, visited_board, words_seen)
    visited_board[i][j] = False
    return words_seen


def boggle_lookup(trie, boggle, i, j, prefix, visited_board, words_seen):
    if '*' in trie:
        words_seen.add(prefix)
    if i < 0 or j < 0 \
            or i >= len(visited_board) or j >= len(visited_board[i]) \
            or visited_board[i][j]:
        return words_seen
    c = boggle[i][j]
    if c not in trie:
        return words_seen
    visited_board[i][j] = True
    # top
    boggle_lookup(trie[c], boggle, i + 1, j, prefix + c, visited_board, words_seen)
    # top-right
    boggle_lookup(trie[c], boggle, i + 1, j + 1, prefix + c, visited_board, words_seen)
    # right
    boggle_lookup(trie[c], boggle, i, j + 1, prefix + c, visited_board, words_seen)
    # bottom-right
    boggle_lookup(trie[c], boggle, i - 1, j + 1, prefix + c, visited_board, words_seen)
    # bottom
    boggle_lookup(trie[c], boggle, i - 1, j, prefix + c, visited_board, words_seen)
    # bottom-left
    boggle_lookup(trie[c], boggle, i - 1, j - 1, prefix + c, visited_board, words_seen)
    # left
    boggle_lookup(trie[c], boggle, i, j - 1, prefix + c, visited_board, words_seen)
    # top-left
    boggle_lookup(trie[c], boggle, i + 1, j - 1, prefix + c, visited_board, words_seen)
    visited_board[i][j] = False
    return words_seen


class MyTestCases(unittest.TestCase):
    def test_boggle_lookup_dfs(self):
        dictionary = {"GEEKS", "FOR", "QUIZ", "GO"}
        boggle = [['G', 'I', 'Z'],
                  ['U', 'E', 'K'],
                  ['Q', 'S', 'E']]
        answers = {'GEEKS'}
        self.assertEqual(
            boggle_lookup_dfs(dictionary, boggle, 0, 0, '', [[False for _ in range(3)] for __ in range(3)], set()), answers)
        answers = {'QUIZ'}
        self.assertEqual(
            boggle_lookup_dfs(dictionary, boggle, 2, 0, '', [[False for _ in range(3)] for __ in range(3)], set()), answers)
        answers = set()
        for i in range(len(boggle)):
            for j in range(len(boggle[i])):
                boggle_lookup_dfs(dictionary, boggle, i, j, '', [[False for _ in range(3)] for __ in range(3)], answers)
        self.assertCountEqual(answers, {'GEEKS', 'QUIZ'})

    def test_boggle_lookup(self):
        dictionary = {"GEEKS", "FOR", "QUIZ", "GO", "FO"}
        t = {}
        for word in dictionary:
            trie = t
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie['*'] = '*'
        boggle = [['G', 'I', 'Z'],
                  ['U', 'E', 'K'],
                  ['Q', 'S', 'E']]
        answers = {'GEEKS'}
        self.assertEqual(
            boggle_lookup(t, boggle, 0, 0, '', [[False for _ in range(3)] for __ in range(3)], set()), answers)
        dictionary = {"dfd", "ded", "fd", "e", "dec", "df"}
        t = {}
        for word in dictionary:
            trie = t
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie['*'] = '*'
        boggle = [['f', 'f'],
                  ['d', 'e'],
                  ['f', 'b'],
                  ['b', 'e']]
        answers = set()
        for i in range(len(boggle)):
            for j in range(len(boggle[i])):
                boggle_lookup(t, boggle, i, j, '', [[False for _ in range(2)] for __ in range(4)], answers)
        self.assertCountEqual(answers, {'fd', 'df', 'e'})


def driver(test_cases):
    for _ in range(test_cases):
        # get dictionary size
        __ = int(input())
        dictionary = {}
        for word in input().split():
            dictionary[word] = True
        n, m = [int(i) for i in input().split()]
        letters = input().split()
        i = 0
        boggle = [['' for _ in range(m)] for __ in range(n)]
        for j in range(n):
            for k in range(m):
                boggle[j][k] = letters[i]
                i += 1


if __name__ == '__main__':
    test_cases = int(input())
    driver(test_cases)
