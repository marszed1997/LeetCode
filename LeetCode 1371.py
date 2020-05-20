# https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/


class Solution:
    def __init__(self):
        self.dict = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

    def findTheLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        bitcnt, ans = 0, 0
        cnt = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        self.pre_dict = {0: 0}
        for id, c in enumerate(s):
            if c not in self.dict:
                if bitcnt in self.pre_dict:
                    ans = max(ans, id + 1 - self.pre_dict[bitcnt])
            else:
                cnt[c] = (cnt[c] + 1) % 2
                if cnt[c] == 0:
                    bitcnt -= self.dict[c]
                else:
                    bitcnt += self.dict[c]
                if bitcnt in self.pre_dict:
                    ans = max(ans, id + 1 - self.pre_dict[bitcnt])
                else:
                    self.pre_dict[bitcnt] = id + 1
        return ans