# https://leetcode-cn.com/problems/subarray-sum-equals-k/


class Solution:
    def __init__(self):
        self.pre = {}

    def subarraySum(self, nums, k):
        """

        :param nums: List[int]
        :param k: int
        :return: int
        """
        self.pre.clear()
        self.pre[0] = 1
        cur_pre = 0
        ans = 0
        for num in nums:
            cur_pre += num
            ans += 0 if (cur_pre - k not in self.pre) else self.pre[cur_pre - k]
            try:
                self.pre[cur_pre] += 1
            except:
                self.pre[cur_pre] = 1
        return ans