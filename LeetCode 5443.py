# https://leetcode-cn.com/contest/weekly-contest-194/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

from queue import PriorityQueue


class Solution:
    def __init__(self):
        self.maxn, self.maxe = 110, 210
        self.fa = [i for i in range(self.maxn)]
        self.chose = [True for i in range(self.maxe)]

        self.q = PriorityQueue()

    def query(self, a):
        if self.fa[a] == a:
            return a
        self.fa[a] = self.query(self.fa[a])
        return self.fa[a]

    def combine(self, a, b):
        faa, fab = self.query(a), self.query(b)
        if faa != fab:
            self.fa[fab] = faa

    def kruskal(self, n, edges, mode, *args):
        while not self.q.empty():
            self.q.get()
        for i in range(n):
            self.fa[i] = i
        for i in range(len(edges)):
            self.q.put((edges[i][2], i, edges[i][0], edges[i][1]))

        sum, sume = 0, 0

        for id in args:
            self.chose[id] = False
            if mode == "mustIn":
                sume += 1
                sum += edges[id][2]
                self.combine(edges[id][0], edges[id][1])

        while not self.q.empty():
            value, idx, a, b = self.q.get()
            if self.chose[idx] is False:
                continue
            faa, fab = self.query(a), self.query(b)
            if faa != fab:
                sume += 1
                sum += value
                self.fa[fab] = faa

        for id in args:
            self.chose[id] = True
        if sume == n - 1:
            return sum
        return -1

    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :param n: int
        :param edges: List[List[int]]
        :return: List[List[int]]
        """
        ans = [[], []]
        minT = self.kruskal(n, edges, "std")
        for i in range(len(edges)):
            tmp = self.kruskal(n, edges, "mustIn", i)
            if tmp == -1 or tmp > minT:
                continue
            tmp = self.kruskal(n, edges, "std", i)
            if tmp == -1 or tmp > minT:
                ans[0].append(i)
            else:
                ans[1].append(i)
        return ans
