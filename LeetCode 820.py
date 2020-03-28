# https://leetcode-cn.com/problems/short-encoding-of-words/


class Trie:
    def __init__(self):
        self.p = 0
        self.trie = [[0 for _ in range(100000)] for _ in range(26)]


class Solution:

    def __init__(self):
        self.T = Trie()

    def InTrie(self, word):
        pos = 0
        for i in range(len(word)):
            pos = self.T.trie[ord(word[i]) - ord('a')][pos]
            if pos == 0:
                return False
        return True

    def minimumLengthEncoding(self, words):
        """
        :param words: List[str]
        :return: int
        """
        ans = 0
        words.sort(key=lambda word: len(word), reverse=True)
        # print(words)
        for word in words:
            word = word[::-1]
            # print(word)
            if self.InTrie(word):
                continue
            pos = 0
            for i in range(len(word)):
                if self.T.trie[ord(word[i]) - ord('a')][pos] != 0:
                    pos = self.T.trie[ord(word[i]) - ord('a')][pos]
                else:
                    # print(self.T.p + 1, word[i])
                    self.T.p += 1
                    self.T.trie[ord(word[i]) - ord('a')][pos] = self.T.p
                    pos = self.T.p
            ans += 1 + len(word)
        return ans