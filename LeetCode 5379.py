class Solution:
    def __init__(self):
        self.n = 50010
        self.dp = [[0 for _ in range(self.n)] for _ in range(2)]

    def stoneGameIII(self, stoneValue):
        """
        :param stoneValue: List[int]
        :return: str
        """
        for i in range(len(stoneValue)):
            self.dp[1][i] = 0x3f3f3f3f
            self.dp[0][i] = -0x3f3f3f3f

        for i in range(len(stoneValue) - 1, -1, -1):
            sum = 0
            for j in range(3):
                if i + j >= len(stoneValue):
                    break
                sum += stoneValue[i + j]
                self.dp[0][i] = max(self.dp[0][i], self.dp[1][i + j + 1] + sum)
                self.dp[1][i] = min(self.dp[1][i], self.dp[0][i + j + 1] - sum)
        if self.dp[0][0] > 0:
            return "Alice"
        if self.dp[0][0] == 0:
            return "Tie"
        return "Bob"