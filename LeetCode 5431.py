# https://leetcode-cn.com/problems/paint-house-iii/


class Solution:
    def __init__(self):
        self.dp = [[[-1 for _ in range(30)] for _ in range(110)] for _ in range(110)]

    def minCost(self, houses, cost, m, n, target):
        """

        :param houses: List[int]
        :param cost: List[List[int]]
        :param m: int
        :param n: int
        :param target: int
        :return:  int
        """
        for i in range(n):
            self.dp[0][0][i + 1] = 0
            # self.dp[0][1][i + 1] = 0
        for idh, house in enumerate(houses):
            if house == 0:
                # print(idh)
                for cur_target in range(idh + 1):
                    for idc, color_cost in enumerate(cost[idh]):
                        if self.dp[idh][cur_target + 1][idc + 1] != -1:
                            self.dp[idh + 1][cur_target + 1][idc + 1] = self.dp[idh][cur_target + 1][idc + 1] + color_cost
                        tmp = 0x3f3f3f3f
                        # print(idh)
                        for i in range(n):
                            # print(idh, cur_target, i + 1, self.dp[idh][cur_target][i + 1])
                            if i != idc and self.dp[idh][cur_target][i + 1] != -1:
                                tmp = min(tmp, self.dp[idh][cur_target][i + 1])
                        if tmp != 0x3f3f3f3f:
                            if self.dp[idh + 1][cur_target + 1][idc + 1] == -1:
                                self.dp[idh + 1][cur_target + 1][idc + 1] = tmp + color_cost
                            else:
                                self.dp[idh + 1][cur_target + 1][idc + 1] = min(
                                    self.dp[idh + 1][cur_target + 1][idc + 1], tmp + color_cost)
            else:
                for cur_target in range(idh + 1):
                    self.dp[idh + 1][cur_target + 1][house] = self.dp[idh][cur_target + 1][house]
                    tmp = 0x3f3f3f3f
                    for i in range(n):
                        if i + 1 == house:
                            continue
                        if self.dp[idh][cur_target][i + 1] != -1:
                            tmp = min(tmp, self.dp[idh][cur_target][i + 1])
                    if tmp != 0x3f3f3f3f:
                        if self.dp[idh + 1][cur_target + 1][house] == -1:
                            self.dp[idh + 1][cur_target + 1][house] = tmp
                        else:
                            self.dp[idh + 1][cur_target + 1][house] = min(self.dp[idh + 1][cur_target + 1][house], tmp)
        if houses[-1] == 0:
            ans = 0x3f3f3f3f
            for i in range(n):
                if self.dp[m][target][i + 1] != -1:
                    ans = min(ans, self.dp[m][target][i + 1])
            if ans == 0x3f3f3f3f:
                return -1
            return ans
        else:
            return self.dp[m][target][houses[-1]]