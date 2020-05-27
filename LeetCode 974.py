# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/


class Solution:
    def __init__(self):
        self.maxk = 10010
        self.mod_k = [0 for _ in range(self.maxk)]

    def subarraysDivByK(self, A, K):
        """
        :param A: List[int]
        :param K: int
        :return: int
        """
        ans = 0
        pre_sum = 0
        self.mod_k[0] = 1
        for i in A:
            pre_sum = (((pre_sum + i) % K) + K) % K
            ans += self.mod_k[pre_sum]
            self.mod_k[pre_sum] += 1
        return ans
