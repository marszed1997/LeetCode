# https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick/


class Solution:
    def __init__(self):
        self.cut_len = []
        self.pre_cut_len = []
        self.dp = [[0x3f3f3f3f for _ in range(110)] for _ in range(110)]

    def minCost(self, n, cuts):
        """
        :param n: int
        :param cuts: List[int]
        :return: int
        """
        cuts.sort()

        tmp = 0
        for i in range(len(cuts) + 1):
            if i == len(cuts):
                self.pre_cut_len.append(n)
                self.cut_len.append(n - tmp)
                self.dp[i][i + 1] = 0
            else:
                self.pre_cut_len.append(cuts[i])
                self.cut_len.append(cuts[i] - tmp)
                self.dp[i][i + 1] = 0
                tmp = cuts[i]

        for i in range(2, len(self.cut_len) + 1):
            for idx, length in enumerate(self.cut_len):
                if idx + i > len(self.cut_len):
                    continue
                if idx == 0:
                    cur_len = self.pre_cut_len[idx + i - 1]
                else:
                    cur_len = self.pre_cut_len[idx + i - 1] - self.pre_cut_len[idx - 1]
                for j in range(idx + 1, idx + i):
                    if i == 3:
                        print(i, idx, j, self.dp[idx][j], self.dp[j][idx + i], cur_len)
                    self.dp[idx][idx + i] = min(self.dp[idx][idx + i], self.dp[idx][j] + self.dp[j][idx + i] + cur_len)
                if i == 3:
                    print(self.dp[idx][idx + i])
        return self.dp[0][len(self.cut_len)]