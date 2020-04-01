# https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/submissions/


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
                self.colorList[id] = self.deep % 2
                self.deep += 1
            else:
                self.deep += 1
                self.colorList[id] = self.deep % 2
        return self.colorList[0: len(seq)]
