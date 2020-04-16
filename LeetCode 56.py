# https://leetcode-cn.com/problems/merge-intervals/
import operator

class Solution:
    def __init__(self):
        self.ans = []

    def merge(self, intervals):
        '''
        :param intervals: List[List[int]]
        :return: List[List[int]]
        '''
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        intervals.sort(key=operator.itemgetter(0, 1))
        cur_intv = intervals[0]
        for id, intv in enumerate(intervals):
            if id == 0:
                continue
            l, r = intv[0], intv[1]
            if l > cur_intv[1]:
                self.ans.append(cur_intv)
                cur_intv = intv
            else:
                cur_intv[1] = max(cur_intv[1], r)
            if id == len(intervals) - 1:
                self.ans.append(cur_intv)
        return self.ans
