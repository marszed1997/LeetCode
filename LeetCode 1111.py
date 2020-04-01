# https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/


class Solution:
    def __init__(self):
        self.deep = 0
        self.colorList = [0 for _ in range(10010)]

    def maxDepthAfterSplit(self, seq):
        """
        :param seq: str
        :return: List[int]
        """
        for id, c in enumerate(seq):
            if c == "(":
                self.colorList[id] = self.deep
                self.deep = (self.deep + 1) % 2
            else:
                self.deep = (self.deep + 1) % 2
                self.colorList[id] = self.deep
        return self.colorList[0: len(seq)]
