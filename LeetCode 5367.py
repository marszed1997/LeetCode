# https://leetcode-cn.com/problems/longest-happy-prefix/


class Solution:

    def __init__(self):
        self.next = [0 for _ in range(100010)]
        self.next[0] = -1

    def getNext(self, s: str):
        i = 1
        j = -1
        while i < len(s):
            if s[i] == s[j + 1]:
                self.next[i] = j + 1
                i += 1
                j += 1
            else:
                if j == -1:
                    self.next[i] = -1
                    i += 1
                else:
                    j = self.next[j]

    def longestPrefix(self, s: str) -> str:
        self.getNext(s)
        if self.next[len(s) - 1] == -1:
            return ""
        return s[: self.next[len(s) - 1]]


