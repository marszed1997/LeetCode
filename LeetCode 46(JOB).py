# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/


class Solution:
    def __init__(self):
        self.ans = [0 for i in range(12)]
        self.ans[0] = 1

    def translateNum(self, num):
        """

        :param num: int
        :return: int
        """
        snum = str(num)
        for id, number in enumerate(snum):
            self.ans[id + 1] = self.ans[id]
            if id >= 1 and 10 <= int(snum[id - 1: id + 1]) <= 25:
                self.ans[id + 1] += self.ans[id - 1]
        return self.ans[len(snum)]