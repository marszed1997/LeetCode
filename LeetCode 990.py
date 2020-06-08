# https://leetcode-cn.com/problems/satisfiability-of-equality-equations/


class Solution:
    def __init__(self):
        self.fa = [i for i in range(30)]

    def query(self, a):
        if self.fa[a] == a:
            return a
        self.fa[a] = self.query(self.fa[a])
        return self.fa[a]

    def combine(self, a, b):
        faa = self.query(a)
        fab = self.query(b)
        if faa != fab:
            self.fa[fab] = faa

    def equationsPossible(self, equations):
        """
        :param equations: List[str]
        :return: bool
        """
        equations.sort(key=lambda x: 0 if x[1] == '=' else 1)
        for eqt in equations:
            a = ord(eqt[0]) - ord('a')
            b = ord(eqt[3]) - ord('a')
            print(a, b)
            if eqt[1] == '=':
                self.combine(a, b)
            else:
                if self.query(a) == self.query(b):
                    return False
        return True
